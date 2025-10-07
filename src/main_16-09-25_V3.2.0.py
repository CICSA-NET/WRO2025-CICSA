# Authors: Iván Hernández, Sergio Hernández & Xiara Alcantar
# Date: September 17, 2025
# Description: This program was developed for the Raspberry Pi 5
#              to execute the obstacle challenge in the Future Engineers
#              category of the WRO 2025 National Stage.
# Target Platform: Raspberry Pi 5 (64-bit, Debian-based OS)
# Language: Python 3.11
# Interfaces: GPIO (PWM, Digital I/O), UART (Serial), I2C (optional)
# Sensors: 3x URM37 V5.0 Ultrasonic Sensors (PWM mode)
# Motor Control: Dual H-Bridge (L298N or equivalent)
# Version: 3.2.0
# License: MIT

import cv2
import numpy as np
import serial
import time
from picamera2 import Picamera2

MIN_CONTOUR_AREA = 500
CRITICAL_CONTOUR_AREA = 4800

# --- CONFIGURATIONS ---
SERIAL_PORT = '/dev/ttyUSB0'
BAUDRATE = 115200
ser = None
lower_red1 = np.array([0, 120, 90])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 90])
upper_red2 = np.array([179, 255, 255])
lower_green = np.array([40, 80, 80])
upper_green = np.array([85, 255, 255])


# --- INITIALIZATION ---
try:
    ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=0.1)
    print(f"Serial Port {SERIAL_PORT} open.")
except serial.SerialException as e:
    print(f"WARNING: Failed to open serial port: {e}")

print("Initializing camera using PREVIEW configuration...")
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()
print("Camera successfully initialized.")
time.sleep(1.0)

frame_test = picam2.capture_array()
FRAME_HEIGHT, FRAME_WIDTH, _ = frame_test.shape

roi_start_x = 40
roi_end_x = 600
roi_start_y = 0 
roi_end_y = FRAME_HEIGHT
print(f"Detected frame: {FRAME_WIDTH}x{FRAME_HEIGHT}. Using ROI in x:({roi_start_x}, {roi_end_x})")
print("Press 'q' in the camera window to exit.")

# --- MAIN LOOP ---
while True:
    # Capture a raw frame from the PiCamera2
    frame_raw = picam2.capture_array()
    
    # Convert the frame from RGB to BGR format (OpenCV uses BGR by default)
    frame = cv2.cvtColor(frame_raw, cv2.COLOR_RGB2BGR)
    
    # Draw a rectangle to visualize the Region of Interest (ROI)
    cv2.rectangle(frame, (roi_start_x, roi_start_y), (roi_end_x, roi_end_y), (255, 255, 0), 2)
    
    # Extract the ROI from the frame for color analysis
    roi = frame[roi_start_y:roi_end_y, roi_start_x:roi_end_x]
    
    # Convert the ROI from BGR to HSV color space for better color segmentation
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    
    # Create two masks to detect red color ranges (to cover hue wrap-around)
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    # Combine both red masks into a single binary mask
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    
    # Create a mask to detect green color range
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    
    # Define a kernel for morphological operations (noise reduction)
    kernel = np.ones((5, 5), np.uint8)
    
    # Apply morphological opening to clean up the red mask
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)
    
    # Apply morphological opening to clean up the green mask
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)
    
    # Find contours in the red mask (external shapes only)
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find contours in the green mask (external shapes only)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize variables to track the critical area (in pixels) occupied by red and green objects
    red_critical_area = 0
    green_critical_area = 0

    # 1. Analyze red contours
    if contours_red:
        # Identify the largest red contour based on area
        largest_red_contour = max(contours_red, key=cv2.contourArea)
        red_area = cv2.contourArea(largest_red_contour)
    
        # Proceed only if the red contour is minimally visible
        if red_area > MIN_CONTOUR_AREA:
            # Draw a bounding box around the red pillar (obstacle)
            x, y, w, h = cv2.boundingRect(largest_red_contour)
            cv2.rectangle(frame, (x + roi_start_x, y), (x + roi_start_x + w, y + h), (0, 0, 255), 2)
    
            # Store its area only if it qualifies as a CRITICAL threat
            if red_area > CRITICAL_CONTOUR_AREA:
                red_critical_area = red_area
    # 2. Analyze green contours
    if contours_green:
        # Identify the largest green contour based on area
        largest_green_contour = max(contours_green, key=cv2.contourArea)
        green_area = cv2.contourArea(largest_green_contour)

        # Proceed only if the green contour is minimally visible
        if green_area > MIN_CONTOUR_AREA:
            # Draw a bounding box around the green pillar (obstacle)
            x, y, w, h = cv2.boundingRect(largest_green_contour)
            cv2.rectangle(frame, (x + roi_start_x, y), (x + roi_start_x + w, y + h), (0, 255, 0), 2)

            # Store its area only if it qualifies as a CRITICAL threat
            if green_area > CRITICAL_CONTOUR_AREA:
                green_critical_area = green_area
    # 3. Compare critical areas and make the final decision
    command_to_send = 'C'  # Default command (e.g., continue or no threat detected)

    if red_critical_area > green_critical_area:
        command_to_send = 'R'  # Red obstacle is dominant — take red avoidance action
    elif green_critical_area > red_critical_area:
        command_to_send = 'G'  # Green obstacle is dominant — take green avoidance action
    elif red_critical_area > 0 and red_critical_area == green_critical_area:
        # In the unlikely case of a tie, give priority to red
        command_to_send = 'R'

    # 4. Send command via serial port
    if ser and ser.is_open:
        try:
            # Encode and transmit the decision command over UART
            ser.write(command_to_send.encode('utf-8') + b'\n')
        except serial.SerialException as e:
            # Print error message if transmission fails
            print(f"Error writing to serial port: {e}")
            
    # 5. Display the image 
    cv2.putText(frame, f"Comando: {command_to_send}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    

# --- FINAL CLEANUP ---
print("Ending program...")
picam2.stop()
if ser and ser.is_open:
    ser.close()
    print("Serial port closed.")
