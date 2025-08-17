import _thread
from machine import Pin, I2C, PWM, time_pulse_us
import time
from time import sleep_ms

# --- Globlal Variables ---
distance_left = 0
distance_right = 0
distance_front = 0
CENTER = 49
LEFT = 25
RIGHT = 68

#determine turn
direction = ""
velocity = 38000

# --- Pin configuration and main modules ---
servo = PWM(Pin(5), freq=50) # Servo motor
servo.duty(CENTER)
led = Pin(2, Pin.OUT)                   # LED interno
led.value(1)
time.sleep(0.25)
led.value(0)

in1 = Pin(18, Pin.OUT)                  # Motor IN1
in2 = Pin(19, Pin.OUT)                  # Motor IN2
enable = PWM(Pin(23), freq=1000)        # Motor PWM enable
enable.duty_u16(0)

# --- Pines para sensor ultrasónico izquierdo y derecho ---
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

# --- Configuración del pulsador ---
button = Pin(13, Pin.IN, Pin.PULL_UP)

# --- Funciónes para obtener distancia ---
def get_distance(echo, trig):
    trig.off()
    time.sleep_us(10)
    trig.on()
    low_time = time_pulse_us(echo, 0, 100000)
    if low_time <= 0 or low_time > 100000:
        return None
    else:
        return int(low_time // 50)  # cada 50 µs ≈ 1 cm

# --- Hilo para lectura continua de sensores ---
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
        
def turn_robot():
    global direction
    global distance_front
    global velocity
    global CENTER
    global LEFT
    global RIGHT
    
    if direction == "right":
        servo.duty(LEFT)  # Giro a la izquierda
        for i in range(21):    #Ajustar valor dependiendo del sensor
            enable.duty_u16(velocity)
            time.sleep(0.001)
        
    if direction == "left":
            servo.duty(RIGHT)  # Giro a la derecha
            for i in range(25):    #Ajustar valor dependiendo del sensor
                enable.duty_u16(velocity)
                time.sleep(0.001)
    servo.duty(CENTER)     # Recentrar

def start_robot():
    global distance_left
    global distance_right
    global direction
    global distance_front
    global velocity
    flag_direction = False
    
    time.sleep(1.5)
    in1.off()
    in2.on()
    enable.duty_u16(40000)
    time.sleep(0.35)
    enable.duty_u16(velocity-13000)
    while not flag_direction:   
        if distance_front <= 65 and distance_left > 100:
            led.value(1)
            flag_direction = True
            direction = "right" # counterclockwise
            servo.duty(LEFT)  # Giro a la izquierda
            for i in range(25):    #Ajustar valor dependiendo del sensor
                enable.duty_u16(velocity)
                time.sleep(0.001)
            
        elif distance_front <= 65 and distance_right > 100:
            led.value(1)
            flag_direction = True
            direction = "left" # clockwise
            servo.duty(RIGHT)  # Giro a la izquierda
            for i in range(21):    #Ajustar valor dependiendo del sensor
                enable.duty_u16(velocity)
                time.sleep(0.001)
        time.sleep(0.1)


# --- PID ---
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
    kp = 1.1     
    ki = 0.01
    kd = 0.25
    T = 0.025
    p_output = 0.0
    count = 0
    p_error = 0.0

    in1.off()
    in2.on()
    enable.duty_u16(int(vel))
    
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
        #mi_lista.append()
        duty = CENTER - output
        duty = min(max(duty, LEFT), RIGHT)
        servo.duty(duty)
        p_output = output
        count += 1
        time.sleep(T)
        if condition == 10000 and distance_front <= 73 and count >= 20:
            break 
    servo.duty(CENTER)
    #print(mi_lista)

#---------------------------------------- main -----------------------------------------
_thread.start_new_thread(get_data, ())
time.sleep(1.5)

# Esperar a que se presione el botón
while button.value() != 0:
    time.sleep(0.1)

try:
    start_robot()
    for i in range(3):
        pid(25, 10000, velocity, direction)
        turn_robot()
    if direction == "left":
        pid(30, 5, velocity, direction)
    enable.duty_u16(0)
    servo.duty(CENTER)
    time.sleep(3)
    
except KeyboardInterrupt:
    servo.duty(CENTER)
    print("End")