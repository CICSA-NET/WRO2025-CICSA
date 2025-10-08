# Authors: Iván Hernández, Sergio Hernández & Xiara Alcantar
# Date: September 17, 2025
# Description: This program was developed for the ESP32 microcontroller
#              to execute the obstacle challenge in the Future Engineers
#              category of the WRO 2025 National Stage.
# Target Platform: ESP32
# Language: MicroPython 1.21
# Interfaces: UART (Serial), PWM, GPIO
# Sensors: 3x URM37 V5.0 Ultrasonic Sensors (PWM mode)
# Motor Control: Dual H-Bridge (L298N)
# Version: 2.2.0

import _thread
from machine import Pin, PWM, UART, time_pulse_us
import time

# =================== Values ===================
velocity = 26000
MANEUVER_BOOST_VELOCITY = velocity + 1000
DIAGONAL_DURATION_MS = 750   # Phase 1: Evasion
TURN_DURATION_MS     = 770   # Phase 2: Evasion (Return)
CORNER_TURN_DURATION_MS = 1800
RECOVERY_FORWARD_MS  = 1050
# End of diagonal movement due to switch with the corresponding lateral unit
DIAG_CHANGE_DELTA_CM = 9    # Minimum shift (in cm) required to interrupt diagonal path
DIAG_MIN_HOLD_MS     = 180  # Minimum wait time before evaluating the change


# Corner position detected
CORNER_DIST_CM        = 20
CORNER_DEBOUNCE_HITS  = 3

# PID 
REF_DIST_CM = 42
KP, KI, KD  = 3.0, 0.01, 0.25
PID_DT      = 0.025

# Servo 
CENTER, LEFT, RIGHT = 43, 19, 62

# Pin
SERVO_PIN   = 5
LED_PIN     = 2
IN1_PIN     = 18
IN2_PIN     = 19
EN_PIN      = 23
ECHO_L, TRIG_L = 15, 4
ECHO_R, TRIG_R = 32, 33
ECHO_F, TRIG_F = 27, 14
BTN_PIN     = 13
UART_TX, UART_RX = 17, 16

# =================== State ===================
distance_left  = 999
distance_right = 999
distance_front = 999

direction = ""     # Wall to follow
integral = 0.0
last_error = 0.0

camera_command = 'C'   # 'R','G','C'

# =================== Hardware ===================
servo = PWM(Pin(SERVO_PIN), freq=50)
led   = Pin(LED_PIN, Pin.OUT)

in1 = Pin(IN1_PIN, Pin.OUT)
in2 = Pin(IN2_PIN, Pin.OUT)
enable = PWM(Pin(EN_PIN), freq=1000)

UR_ECHO_LEFT  = Pin(ECHO_L, Pin.IN); UR_TRIG_LEFT  = Pin(TRIG_L,  Pin.OUT)
UR_ECHO_RIGHT = Pin(ECHO_R, Pin.IN); UR_TRIG_RIGHT = Pin(TRIG_R,  Pin.OUT)
UR_ECHO_FRONT = Pin(ECHO_F, Pin.IN); UR_TRIG_FRONT = Pin(TRIG_F,  Pin.OUT)

button = Pin(BTN_PIN, Pin.IN, Pin.PULL_UP)
uart   = UART(2, baudrate=115200, tx=UART_TX, rx=UART_RX, timeout=0)

# =================== Motors ===================
def set_speed_forward(pwm):
    in1.off(); in2.on()
    enable.duty_u16(max(0, min(65535, pwm)))

def set_speed_reverse(pwm):
    in1.on(); in2.off()
    enable.duty_u16(max(0, min(65535, pwm)))

def stop_motors():
    enable.duty_u16(0)

# =================== Sensors ===================
def get_distance(echo: Pin, trig: Pin) -> int:
    trig.off(); time.sleep_us(10); trig.on()
    t = time_pulse_us(echo, 0, 100000)
    return 999 if (t is None or t <= 0) else int(t // 50)  # ~cm aprox

def sensor_thread():
    global distance_left, distance_right, distance_front
    while True:
        distance_front = get_distance(UR_ECHO_FRONT, UR_TRIG_FRONT)
        time.sleep_ms(20)
        distance_right = get_distance(UR_ECHO_RIGHT, UR_TRIG_RIGHT)
        time.sleep_ms(20)
        distance_left  = get_distance(UR_ECHO_LEFT,  UR_TRIG_LEFT)
        time.sleep_ms(20)

# =================== UART ===================
def poll_uart():
    """Lee el último comando R/G/C disponible y lo aplica."""
    global camera_command
    b = uart.read()
    if not b: return
    for byte in b:
        ch = chr(byte).upper()
        if ch in ('R', 'G', 'C'):
            camera_command = ch

# =================== Start ===================
def start():
    global direction
    # Wait for button press
    while button.value() != 0:
        time.sleep_ms(10)

    # Startup
    in1.off(); in2.on()
    enable.duty_u16(velocity)
    servo.duty(CENTER)

    # Auto-detect wall to follow
    t0 = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), t0) < 1000:
        if distance_left <= 30:  direction = "left";  break
        if distance_right <= 30: direction = "right"; break
        time.sleep_ms(20)
    led.on()

# =================== Control ===================
def pid_step():
    # One PID step following the selected wall
    global integral, last_error
    set_speed_forward(velocity)

    if direction == "left":
        # Calculate error based on left wall distance
        error = distance_left - REF_DIST_CM
    
        # Compute PID output using proportional, integral, and derivative terms
        output = KP * error + KI * integral + KD * (error - last_error)
    
        # Adjust motor duty cycle to steer away from left wall
        duty = CENTER - int(output)
    else:
        # Calculate error based on right wall distance
        error = REF_DIST_CM - distance_right
    
        # Compute PID output using proportional, integral, and derivative terms
        output = KP * error + KI * integral + KD * (error - last_error)
    
        # Adjust motor duty cycle to steer away from right wall
        duty = CENTER + int(output)

    integral += error
    last_error = error

    # Servo limits
    if duty < LEFT: duty = LEFT
    if duty > RIGHT: duty = RIGHT
    servo.duty(duty)

def execute_lane_change(color):
    
    turn, counter = (RIGHT, LEFT) if color == 'R' else (LEFT, RIGHT)

    # Take initial reference readings
    base_left  = distance_left
    base_right = distance_right

    enable.duty_u16(MANEUVER_BOOST_VELOCITY)
    servo.duty(turn)
    t0 = time.ticks_ms()

    while True:
        now = time.ticks_ms()
        elapsed = time.ticks_diff(now, t0)

        # Avoid false positives during initial milliseconds
        if elapsed >= DIAG_MIN_HOLD_MS:
            if color == 'R':
                # R: cortar cuando LEFT cambie lo suficiente
                if distance_left < 990 and abs(distance_left - base_left) >= DIAG_CHANGE_DELTA_CM:
                    break
            else:
                # G: stop when RIGHT changes significantly
                if distance_right < 990 and abs(distance_right - base_right) >= DIAG_CHANGE_DELTA_CM:
                    break

        # Safety stop
        if elapsed >= DIAGONAL_DURATION_MS:
            break

        time.sleep_ms(10)
    servo.duty(counter); time.sleep_ms(TURN_DURATION_MS)
    servo.duty(CENTER); set_speed_forward(velocity)        
    time.sleep_ms(RECOVERY_FORWARD_MS)
    servo.duty(counter); time.sleep_ms(TURN_DURATION_MS)
    servo.duty(turn);    time.sleep_ms(DIAGONAL_DURATION_MS)


def execute_corner_turn():
    # Corner turn based on fixed time, respecting wall direction
    turn_dir = LEFT if direction == "left" else RIGHT
    set_speed_reverse(MANEUVER_BOOST_VELOCITY)
    servo.duty(turn_dir); time.sleep_ms(CORNER_TURN_DURATION_MS)
    servo.duty(CENTER)
    turn_dir = RIGHT if direction == "left" else LEFT
    set_speed_forward(MANEUVER_BOOST_VELOCITY)
    servo.duty(turn_dir); time.sleep_ms(1350)
    servo.duty(CENTER)
    set_speed_reverse(MANEUVER_BOOST_VELOCITY)
    time.sleep_ms(2500)
    
# =================== Main ===================
def main():
    global camera_command, integral, last_error
    servo.duty(CENTER)
    UR_TRIG_FRONT.on(); UR_TRIG_LEFT.on(); UR_TRIG_RIGHT.on()
    _thread.start_new_thread(sensor_thread, ())

    start()
    corner_hits = 0

    while True:
        poll_uart()

        # 1) Pillars detected via camera
        if camera_command in ('R', 'G'):
            c = camera_command
            camera_command = 'C'
            execute_lane_change(c)
            
            # Short recovery
            integral = 0; last_error = 0
            servo.duty(CENTER)
            continue

        # 2) Wall-following PID
        pid_step()
        time.sleep(PID_DT)

        # 3) Corner 
        if distance_front <= CORNER_DIST_CM:
            corner_hits += 1
        else:
            corner_hits = 0

        if corner_hits >= CORNER_DEBOUNCE_HITS:
            execute_corner_turn()
            integral = 0; last_error = 0
            servo.duty(CENTER); set_speed_forward(velocity)
            time.sleep_ms(RECOVERY_FORWARD_MS)
            corner_hits = 0

# =================== Run ===================
try:
    main()
except KeyboardInterrupt:
    stop_motors(); servo.duty(CENTER); led.off()



