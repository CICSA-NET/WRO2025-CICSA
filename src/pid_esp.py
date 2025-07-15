import _thread
from machine import Pin, PWM, I2C
from time import sleep
from vl53l0x import VL53L0X

# --- Configuración de pines y módulos principales ---
servo = PWM(Pin(5), freq=50)            # Servo motor
led = Pin(2, Pin.OUT)                   # LED interno
led.value(1)
sleep(0.25)
led.value(0)

in1 = Pin(18, Pin.OUT)                  # Motor IN1
in2 = Pin(19, Pin.OUT)                  # Motor IN2
enable = PWM(Pin(21), freq=1000)        # Motor PWM enable

# --- Buses I2C para sensores VL53L0X ---
i2c_left = I2C(1, sda=Pin(32), scl=Pin(33), freq=100000)   # Sensor izquierdo
i2c_right = I2C(0, sda=Pin(25), scl=Pin(26), freq=100000)  # Sensor derecho

vl53_left = VL53L0X(i2c_left)
vl53_right = VL53L0X(i2c_right)

# --- Función de lectura de sensores VL53L0X ---
def leer_sensores():
    distancia_izq = int(vl53_left.ping())
    distancia_der = int(vl53_right.ping())
    if distancia_izq < 200:
        return "left"
    elif distancia_der < 200:
        return "right"
    else:
        return "ninguno"

# --- Algoritmo PID para ajuste de movimiento ---
def pid(ref, condicion, vel, sensor):
    output = 0.0
    error = 0.0
    p_error_2 = 0.0
    kp = 30
    ki = 0.1
    kd = 6.3
    T = 0.01
    p_output = 0.0
    count = 0
    p_error = 0.0

    # Activar motor con aceleración progresiva
    for d in range(400, int(vel / 65535 * 1023), 100):
        enable.duty(d)
        sleep(0.05)

    in1.off()       # Ajusta dirección si tu robot retrocede
    in2.on()

    while count <= condicion:
        p_error_2 = p_error
        p_error = error
        if sensor == "left":
            input_sensor = int(vl53_left.ping())
            error = input_sensor - ref
        elif sensor == "right":
            input_sensor = int(vl53_right.ping())
            error = ref - input_sensor
        else:
            input_sensor = ref

        output = int(kp * (error - p_error) + ki * error + kd * (error - (2 * p_error) + p_error_2) + p_output)
        duty = 6650 - output
        duty = min(max(duty, 4750), 7850)
        servo.duty(int(duty / 65535 * 1023))  # Conversión PWM para ESP32

        p_output = output
        count += 1
        sleep(T)

    enable.duty(0)
    servo.duty(int(6650 / 65535 * 1023))

# --- Programa principal ---
try:
    led.value(1)
    servo.duty(int(6650 / 65535 * 1023))
    sleep(1.5)

    sensor_detectado = leer_sensores()
    if sensor_detectado in ["left", "right"]:
        pid(250, 250, 40000, sensor_detectado)  # Máxima potencia segura

    enable.duty(0)
    servo.duty(int(6650 / 65535 * 1023))
    led.value(0)

except KeyboardInterrupt:
    print("Fin")