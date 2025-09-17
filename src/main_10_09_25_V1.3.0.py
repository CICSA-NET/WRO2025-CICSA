# Autores: Xiara Alcantar, Iván Hernández & Sergio Hernández.
# Fecha: 17 de septiembre de 2025
# Descripción: Este programa fue desarrollado para el reto  libre
#              de la competencia Future Engineers de la WRO 2025 Etapa Nacional.
# Versión: 1.3.0

import _thread
from machine import Pin, I2C, PWM, time_pulse_us
import time
from time import sleep_ms

# --- Globlal Variables ---
distance_left = 0
distance_right = 0
distance_front = 0
CENTER = 43      #48
LEFT = 20        #25
RIGHT = 60       #68

#determine turn
direction = ""
velocity = 30000                                                          

# --- Pin configuration and main modules ---
servo = PWM(Pin(5), freq=50) # Servo motor
servo.duty(CENTER)
time.sleep_ms(500)
led = Pin(2, Pin.OUT)                   # LED 
led.value(1)
time.sleep(0.25)
led.value(0)

in1 = Pin(18, Pin.OUT)                  # Motor IN1
in2 = Pin(19, Pin.OUT)                  # Motor IN2
enable = PWM(Pin(23), freq=1000)        # Motor PWM enable
enable.duty_u16(0)

# --- sensors ---
UR_ECHO_LEFT = Pin(15, Pin.IN)   
UR_TRIG_LEFT = Pin(4, Pin.OUT)
UR_ECHO_RIGHT = Pin(32, Pin.IN)   
UR_TRIG_RIGHT = Pin(33, Pin.OUT)
UR_ECHO_FRONT = Pin(27, Pin.IN)
UR_TRIG_FRONT = Pin(14, Pin.OUT)      
UR_TRIG_LEFT.on()                  
time.sleep_ms(500)
UR_TRIG_RIGHT.on()                  
time.sleep_ms(500)
UR_TRIG_FRONT.on()
time.sleep_ms(500)

# --- sw ---
button = Pin(13, Pin.IN, Pin.PULL_UP)

# --- Functions ---
# turn around
def turn_servo(value):
    for i in range(3):
        servo.duty(value)
        time.sleep_us(100)
        
# Get data from distance sensors
def get_distance(echo, trig):
    trig.off()
    time.sleep_us(10)
    trig.on()
    low_time = time_pulse_us(echo, 0, 100000)
    if low_time <= 0 or low_time > 100000:
        return None
    else:
        return int(low_time // 50)  # cada 50 µs ≈ 1 cm

def get_data():
    global distance_left
    global distance_right
    global distance_front

    while True:     
        distance_front = get_distance(UR_ECHO_FRONT, UR_TRIG_FRONT) 
        time.sleep_ms(5)
        distance_right = get_distance(UR_ECHO_RIGHT, UR_TRIG_RIGHT)
        time.sleep_ms(5)
        distance_left = get_distance(UR_ECHO_LEFT, UR_TRIG_LEFT)
        time.sleep_ms(5)
# turn around      
def turn_robot():
    global direction
    global distance_front
    global velocity
    global CENTER
    global LEFT
    global RIGHT
    
    if direction == "right":
        servo.duty(LEFT)  # left
        for i in range(22):   
            servo.duty(LEFT)
            enable.duty_u16(velocity + 8000)
            time.sleep(0.001)
        
    if direction == "left":
        servo.duty(RIGHT)  # right
        for i in range(23):    
            servo.duty(RIGHT) 
            enable.duty_u16(velocity + 8000)
            time.sleep(0.001)
    turn_servo(CENTER)   # center
    time.sleep(0.1)
    
# Start, identify meaning.
def start_robot():
    global distance_left
    global distance_right
    global direction
    global distance_front
    global velocity
    global CENTER
    global LEFT
    global RIGHT
    flag_direction = False
    
    in1.off()
    in2.on()
    enable.duty_u16(45000)
    time.sleep(0.35)
    enable.duty_u16(velocity - 6000)
    
    while not flag_direction:
        time.sleep(0.01)
        if distance_left > 100:
            direction = "right" # counterclockwise
            if distance_front > 60 and flag_direction == False :
                time.sleep(0.25)
                flag_direction = True
                servo.duty(LEFT)  # left
                enable.duty_u16(velocity + 10000) 
                for i in range(22):    #Ajustar valor dependiendo del sensor
                    servo.duty(LEFT)  # Giro a la izquierda
                    time.sleep(0.001)
                 
            if distance_front < 60 and flag_direction == False :
                flag_direction = True
                enable.duty_u16(0)
                time.sleep(0.2)
                in1.on()
                in2.off()
                while True:
                    enable.duty_u16(velocity)
                    if distance_front >= 55:
                        break
                    time.sleep(0.001)
                enable.duty_u16(0)
                time.sleep(0.2)
                in1.off()
                in2.on()
                enable.duty_u16(velocity)
                time.sleep(0.85)
                enable.duty_u16(velocity + 10000)
                for i in range(33):
                    time.sleep(0.001)
                    servo.duty(LEFT)  # left
                    
        #******************************************************       
        elif distance_right > 100:
            direction = "left" # clockwise
            if distance_front > 60 and flag_direction == False :
                time.sleep(0.25)
                flag_direction = True
                servo.duty(RIGHT)  # right
                enable.duty_u16(velocity + 10000)
                for i in range(22):  
                    servo.duty(RIGHT)  # right
                    time.sleep(0.001)
                
            if distance_front < 60 and flag_direction == False :
                flag_direction = True
                enable.duty_u16(0)
                time.sleep(0.1)
                in1.on()
                in2.off()
                while True:
                    enable.duty_u16(velocity)
                    if distance_front >= 55:
                        break
                    time.sleep(0.001)
                enable.duty_u16(0)
                time.sleep(0.2)
                in1.off()
                in2.on()
                enable.duty_u16(velocity)
                time.sleep(0.85)
                enable.duty_u16(velocity + 10000)
                for i in range(33):
                    time.sleep(0.001)
                    servo.duty(RIGHT)  # right
                    
    turn_servo(CENTER)   # center
    time.sleep(0.15)

# --- PID control algorithm ---
def pid(ref, condition, vel, sensor):
    global distance_left
    global distance_right
    global distance_front
    global CENTER
    global LEFT
    global RIGHT
    flag_ref=False
    output = 0.0
    error = 0.0
    p_error_2 = 0.0
    kp = 1.4        
    ki = 0.01
    kd = 0.25
    T = 0.015
    p_output = 0.0
    count = 0
    p_error = 0.0

    led.value(1)
    in1.off()
    in2.on()
#     Start the control algorithm
    enable.duty_u16(vel)
    while count <= condition:
        p_error_2 = p_error
        p_error = error
        if sensor == "left":
            input_sensor = distance_left
            error = input_sensor - ref
        elif sensor == "right":
            input_sensor = distance_right
            error = ref - input_sensor
        output = int(kp * (error - p_error) + ki * error + kd * (error - (2 * p_error) + p_error_2) + p_output)
        duty = CENTER - output
        duty = min(max(duty, LEFT), RIGHT)
        servo.duty(duty)
        p_output = output
        count += 1
        time.sleep(T)
        
        if condition == 10000 and distance_front <= 73 and count >= 15:
            break
        
    turn_servo(CENTER)   # center
    led.value(0)
#---------------------------------------- main -----------------------------------------
_thread.start_new_thread(get_data, ())
time.sleep(1.5)

# Wait start
led.value(1)
while button.value() != 0:
    time.sleep(0.1)
led.value(0)
# Main program
try:
    start_robot()
    #pid(25, 10000, velocity, direction)
    #turn_robot()
    for i in range(3):
        pid(25, 10000, velocity, direction)
        turn_robot()
    if direction == "right":
        pid(30, 4, velocity, direction)
        #turn_servo(LEFT)
    if direction == "left":
        pid(30, 5, velocity, direction)
        #turn_servo(RIGHT)

    enable.duty_u16(0)
    time.sleep(1)
    turn_servo(CENTER)   # Center
    
except KeyboardInterrupt:
    turn_servo(CENTER)   # Center

