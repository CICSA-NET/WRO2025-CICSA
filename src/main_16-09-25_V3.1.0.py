
import cv2
import numpy as np
import serial
import time
from picamera2 import Picamera2

MIN_CONTOUR_AREA = 500
CRITICAL_CONTOUR_AREA = 4800

# --- CONFIGURACIONES  ---
SERIAL_PORT = '/dev/ttyUSB0'
BAUDRATE = 115200
ser = None
lower_red1 = np.array([0, 120, 90])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 90])
upper_red2 = np.array([179, 255, 255])
lower_green = np.array([40, 80, 80])
upper_green = np.array([85, 255, 255])


# --- INICIALIZACIÓN (Sin cambios) ---
try:
    ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=0.1)
    print(f"Puerto serie {SERIAL_PORT} abierto.")
except serial.SerialException as e:
    print(f"ADVERTENCIA: No se pudo abrir el puerto serie: {e}")

print("Inicializando cámara usando la configuración de PREVIEW...")
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()
print("Cámara iniciada con éxito.")
time.sleep(1.0)

frame_test = picam2.capture_array()
FRAME_HEIGHT, FRAME_WIDTH, _ = frame_test.shape

roi_start_x = 40
roi_end_x = 600
roi_start_y = 0 
roi_end_y = FRAME_HEIGHT
print(f"Frame detectado: {FRAME_WIDTH}x{FRAME_HEIGHT}. Usando ROI en x:({roi_start_x}, {roi_end_x})")
print("Presiona 'q' en la ventana de la cámara para salir.")

# --- BUCLE PRINCIPAL ---
while True:
    frame_raw = picam2.capture_array()
    frame = cv2.cvtColor(frame_raw, cv2.COLOR_RGB2BGR)
    
    cv2.rectangle(frame, (roi_start_x, roi_start_y), (roi_end_x, roi_end_y), (255, 255, 0), 2)
    roi = frame[roi_start_y:roi_end_y, roi_start_x:roi_end_x]

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    kernel = np.ones((5, 5), np.uint8)
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    ### NUEVA LÓGICA DE DECISIÓN JUSTA ###
    
    red_critical_area = 0
    green_critical_area = 0

    # 1. Analizar contornos rojos
    if contours_red:
        largest_red_contour = max(contours_red, key=cv2.contourArea)
        red_area = cv2.contourArea(largest_red_contour)
        if red_area > MIN_CONTOUR_AREA:
            # Dibujamos el pilar rojo si es mínimamente visible
            x,y,w,h = cv2.boundingRect(largest_red_contour)
            cv2.rectangle(frame, (x+roi_start_x, y), (x+roi_start_x+w, y+h), (0,0,255), 2)
            # Guardamos su área solo si es una amenaza CRÍTICA
            if red_area > CRITICAL_CONTOUR_AREA:
                red_critical_area = red_area
    
    # 2. Analizar contornos verdes
    if contours_green:
        largest_green_contour = max(contours_green, key=cv2.contourArea)
        green_area = cv2.contourArea(largest_green_contour)
        if green_area > MIN_CONTOUR_AREA:
            # Dibujamos el pilar verde si es mínimamente visible
            x,y,w,h = cv2.boundingRect(largest_green_contour)
            cv2.rectangle(frame, (x+roi_start_x, y), (x+roi_start_x+w, y+h), (0,255,0), 2)
            # Guardamos su área solo si es una amenaza CRÍTICA
            if green_area > CRITICAL_CONTOUR_AREA:
                green_critical_area = green_area

    # 3. Comparar las áreas críticas y tomar la decisión final
    command_to_send = 'C'
    if red_critical_area > green_critical_area:
        command_to_send = 'R'
    elif green_critical_area > red_critical_area:
        command_to_send = 'G'
    elif red_critical_area > 0 and red_critical_area == green_critical_area:
        # En caso de un empate improbable, damos preferencia a uno (ej. Rojo)
        command_to_send = 'R'

    # 4. Enviar comando (sin cambios)
    if ser and ser.is_open:
        try:
            ser.write(command_to_send.encode('utf-8') + b'\n')
        except serial.SerialException as e:
            print(f"Error al escribir en el puerto serie: {e}")
            
    # 5. Mostrar la imagen (sin cambios)
    cv2.putText(frame, f"Comando: {command_to_send}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    

# --- LIMPIEZA FINAL ---
print("Terminando programa...")
picam2.stop()
if ser and ser.is_open:
    ser.close()
    print("Puerto serie cerrado.")