
<img width="842" height="468" alt="image" src="https://github.com/user-attachments/assets/f008d91d-e2a0-4c5f-97a4-c56cfcc7fe91" />

This is the official repository of the Team CICSA for the international final of the WRO2025 season in Panamá.

## Contents.
**Folders**
- [📁 Models](./models/)
- [📁 Schemes](./schemes/)
- [📁 Src](./src/)
- [📁 T-photos](./t-photos/)
- [📁 V-photos](./v-photos/)
- [📁 Video](./video/)

**Index**

- [The team](#The-team)
- [The Challenge.](#The-Challenge)
- [Robot Overview](#Robot-Overview)
- [Robot construction guide.](#Robot-construction-guide)
- [Engineering materials](#Engineering-materials)
- [Mobility Management](#Mobility-Management)
- [Power and Sensor Management](#Power-and-Sensor-Management)
- [Obstacle management](#Obstacle-management)
- [Work log](#Work-log)
- [References](#References)

___
## The team.
====

CICSA WRO 2025 - Future Engineers

Coach **Sergio Iván Hernández Ruiz**

Coach Sergio Iván provides the technical guidance and leadership required to keep Team CICSA on track. With extensive experience in robotics, he helps us navigate complex challenges, refine our designs, and develop solutions that work in competitive and real-world settings.

Sergio Iván has been the director of the CICSA robotics academy since 2015 and has participated in events organized by the WRO since 2019.
***
**Members:**

**Iván Ramón Hernández Gónzalez**, at 21 years old, he studies Electronics Engineering at the Instituto Tecnológico de Nogales. He participated in the WRO regional competition in 2019, obtaining 1st place in the preparatory category in the city of Guadalajara, Jalisco, México. In 2024, he was the coach of the CICSA team that participated in the ChampionShip of Italy, with an outstanding performance. In 2025, he participated as a coach in the Robotics Championship, an event affiliated with the Baja Robotics League, in Tijuana, Baja California, México, obtaining 2nd place in the Zumo Kit educational competitions category.
***
**Sergio Amid Hernández Gónzalez**, at 19 years old, he studies Software Engineering at Kuepa University. He has participated in numerous competitions, including: the 2019 WRO Regional in Guadalajara, Jalisco, México, where he obtained 1st place. In 2024, in the city of Mexicali, Baja California, México, they obtained 1st place in the preparatory category. He was part of the Mexican robotics team that represented Mexico at the ChampionShip in Italy in 2024.
***
**Xiara Gabriela Alcantar Dorame**, she is 19 years old, studies Mechatronics Engineering at the Universidad Tecnológica de Nogales, in 2020 she was part of the CICSA team that would represent CICSA in the regional competition, but the pandemic prevented the event from taking place, for 2025 she will be part of the CICSA representative in the National competition in Rosarito, Baja California, México.

___

<img width="222" height="315" alt="image" src="https://github.com/user-attachments/assets/0967d148-6391-4b47-a9ea-2ec88d4f37e1" />



[Menu](#Contents)

___

## The Challenge.
====

The WRO Future Engineers challenge pushes students to create fully autonomous self-driving vehicles. Each robot must:

- Navigate a dynamically randomized track.
- Detect and avoid colored obstacles (green/red blocks).
- Execute a parallel parking maneuver.

Scoring is based on:
- Performance on track.
- Obstacle handling.
- Documentation quality.
- Innovation and engineering rigor.

Objective:
Design and build a mobile robot capable of autonomous navigation using: 
* Image recognition for object detection.
* PID control to maintain a safe distance from obstacles using ultrasonic sensors.
* Communication between Raspberry Pi 5 and ESP32 to divide tasks between heavy processing (vision) and real-time control (motors and sensors).

**Open challenge.**

<img width="817" height="459" alt="image" src="https://github.com/user-attachments/assets/ff3d98e8-99d8-4e3b-b802-f49cc1a7c85c" />



**Obstacle challenge.**

<img width="963" height="552" alt="image" src="https://github.com/user-attachments/assets/ebe243d9-7ccf-4ea6-b62b-a09898a56666" />


For more indo visit: [WRO Official Site](https://wro-association.org/)


[Menu](#Contents)
___

## Robot Overview.
====

| Front | Back | Top |
|---------------|---------------|----------------|
| ![](v-photos/Robot_Front.jpeg) | ![](v-photos/Robot_back.jpeg) | ![](v-photos/Robot_Top.jpeg) |

| Bottom | Left | Right |
|---------------|---------------|----------------|
| ![](v-photos/Robot_Bottom.jpeg) | ![](v-photos/Robot_Left.jpeg) | ![](v-photos/Robot_Right.jpeg) |


| Side Dimensions | Front Dimensions | Robot Weight| 
|---------------|---------------|----------------|
| ![](v-photos/Side_Dimensions.jpeg) | ![](v-photos/Front_Dimensions.jpeg) | ![](v-photos/Robot_Weight.jpeg) |



[Menu](#Contents)
___

## Robot construction guide.
====

**Assembly Guide.**

This guide provides step-by-step instructions for assembling the robot chassis. It includes mechanical installation, electrical wiring, and safety notes for robotics projects using ESP-32, Raspberry Pi 5, camera and sensors.

---

**Component List.**

| Component                   | Quantity | Description                     |
|----------------------------|----------|---------------------------------|
| JGA25-370 DC Motor         | 1        | Gear motor for drive system     |
| Servo Motor                | 1        | For front steering mechanism    |
| Wheels                     | 4        | Includes M4 nuts                |
| Bearings (large/small)     | 8        | 2 per wheel                     |
| Steering Cup               | 2        | For front wheels                |
| Short Ball Head            | 1        | Connects servo to steering cup |
| Steering Rod               | 2        | Length: 65 mm                   |
| M3×5mm Screws              | 4        | Servo mounting                  |
| M3×8mm Screws              | 4        | Pillar mounting                 |
| M2.5×10mm Screws           | 2        | Steering rod mounting           |
| M3×22mm Copper Pillars     | 4        | Standard chassis height         |
| M3×16mm Copper Pillars     | 4        | Extended front option           |
| Rocker Switch              | 1        | Power control                   |

---

**Pre-Installation Checks.**

**Servo Motor.**
- Connect and calibrate to **90°** before installation.
- Use test code or compatible software.

**DC Motor.**
- Power directly to verify rotation.
- **Red dot** indicates positive terminal.

---

**Wheel Assembly Steps.**

1. Insert rotating shaft.
2. Add large bearing.
3. Install steering cup.
4. Add small bearing.
5. Insert pin.
6. Attach hex coupler.
7. Mount wheel.
8. Secure with M4 nut.

>  Ensure bearings are parallel and wheel rotates freely.

---

**Servo & Steering Assembly.**

- Mount servo to L-bracket using M3×5mm screws.
- Connect short ball head between servo and steering cup.
- Attach steering rods using M2.5×10mm screws.

---

**Chassis Mounting.**

- Use M3×22mm pillars and M3×8mm screws for standard setup.
- For extended front space (e.g. larger battery), use M3×16mm pillars.
- [Place the base to hold the connector](models/base_conector_v3.STL)
- [Place the base to hold the L298N](models/base_l298n.stl)
- [Place the main base](models/base_principal_V6.STL)
- [Place the base to hold the support of the camera](models/base_camera_v2.STL)
- [Place the base to hold the camera](models/base_camera2_V2.STL)
- [Place the camera base cover](models/tapa_camera.STL)
- [Place the base to hold the sensors UM](models/base_urm37_v7.STL)
- [Place the base to hold the Rasoberry Pi 5](models/Base_Pi_5_v5.STL)
- [Place the shield that contains the esp32](https://www.mercadolibre.com.mx/screw-shield-adaptador-de-terminales-esp32-30-pines/p/MLM2038781113?pdp_filters=item_id%3AMLM2162499429#origin%3Dshare%26sid%3Dshare)

For more information regarding 3D printed parts: [📁 Models](./models/)

---

**Electrical Wiring.**

**Servo Motor.**

| Wire Color | Function |
|------------|----------|
| Brown      | GND      |
| Red        | VCC      |
| Yellow     | Signal   |

**Power Switch.**

- Connect **in series** with the positive (red) wire.
- Enables safe power control.

---

**Safety Notes.**

- Do not operate in humid environments.
- Avoid reverse polarity.
- Prevent short circuits.
- Double-check connections before powering on.

---

**Board Compatibility.**

Mounting holes support:

- ESP-32 base
- Camera base
- Raspberry Pi 5 base

---

Original PDF: [Elecrow 4WD Car Installation Instructions](https://www.elecrow.com/download/4wd_CAR_Install_instructions.pdf)

---




[Menu](#Contents)
___



## Engineering materials.
====

This repository contains engineering materials of a self-driven vehicle's model participating in the WRO Future Engineers competition in the season 2025.

| Quantity | Component                        |Link                                                                            |
|----------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1        | Raspberry Pi 5 (16GB)             |[Amazon](https://www.amazon.com/gp/product/B0DSPYPKRG/ref=ox_sc_act_title_6?smid=A02211013Q5HP3OMSZC7W&psc=1)                                                                                                                                                                                                                                            |
| 1        | ESP-WROOM-32                     |[Amazon](https://www.amazon.com/ESP-WROOM-32-Development-Microcontroller-Integrated-Compatible/dp/B08D5ZD528/ref=sr_1_3?crid=4UOP8VE8GTTS&dib=eyJ2IjoiMSJ9.XBINg-sjhfF_gUtnMiKGjjEQQzaaOnS0BOX5B4WtqfKi_hDEOXP7QQezpOTp8e-r5VfFo411y5_IeCcg7DdMeiEcUBSTnC23mXHz1NRbrXP4JVyQShmo1b-y4KGfxRlXgSbH3VJTSz55fBe_QqxKedXkggHhw1Qs7-1O_ErcV1o19Py9to1BKZQxieZLm_8y4zb-6LtXq2DwHFZG0EPFL_AJ_bL6bAtaLzdAk6A-5WPFche0M6tcFhuRjMkOpAN2zYFYcGYeWiFqfLdcRUPoiY2-8jpuuo8vkBUfver4Gk4.mo41uc2rmPqL0XJ5jHK3kmN_x8PFmvrfhMfZ2HkptCM&dib_tag=se&keywords=Esp-Wroom-32&qid=1753387413&s=electronics&sprefix=esp-wroom-32%2Celectronics%2C294&sr=1-3&th=1)                                                                                                                                                                              |
| 1        | Camara Freenove 8MP              |[Amazon](https://www.amazon.com/Freenove-8MP-Raspberry-Adjustable-Viewing/dp/B0BZYPBS17/ref=sr_1_1_sspa?crid=2ZNF0R4SWCQWT&dib=eyJ2IjoiMSJ9.f4-pR4WTqQbw0vioJRPdz0qtF5MiHJl-MhiG_Yo9dxwZXPo4CsqP2Iiyt_ae639ZQ68gVBs98taIG5zMf0PXKR6IMyUoCDn_jD7_hGgcOXlWreSjEqpqQpZTBdGct0sKvzvACoLi4qHOlHhM0e-xMC_308CRUrspoesSuOSSsMM.nVcijt2RJWCE17iYMeWy3e3SG6eqijPvlEt37sYoc44&dib_tag=se&keywords=Freenove%2B8MP%2Bcamera&qid=1753387520&s=electronics&sprefix=freenove%2B8mp%2Bcamera%2Celectronics%2C285&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)                                                                                                                                                                              |
| 1        | Driver de motor L298N            |[Amazon](https://www.amazon.com/JTAREA-Stepper-Driver-H-Bridge-Mega2560/dp/B0D2RJV2VX/ref=sr_1_2_sspa?crid=3C1LW4P6C7MR1&dib=eyJ2IjoiMSJ9.hK2FjV8Ukp8CCyVTI1seMoTh-okctAQYG9wv8_2wWQicu3tQcZGLcWqQEfZJZiEpCHtA15XAfvFsTRtoXRJ6wEG8xSTcdPfjtlfmyDqol-3C38gVuPnv3FlabrIutV5q3wzdwbimQaUZF726_CESUC5PDSaG-sz7VeI6AP5hrkIpA2wr_m-ZQoxYgSgCYoBXOSU32LgaoI1_3YNdT_o4-caslfve1JPRLD6TIg68hNFwg8Zbz9FSaIh7d_UwKp6OgV7lm5ut-c0lOlitzyWm5AU5nTyhq4AwX1OCGBCl33Y.P4ZzI9RZbRt-hM7EfbWZSR7GTTefFCgTi5MY6UKLEI0&dib_tag=se&keywords=L298N%2Bmotor%2Bdriver&qid=1753387552&s=electronics&sprefix=l298n%2Bmotor%2Bdriver%2Celectronics%2C173&sr=1-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)                                                                                                                                                                             |
| 1        | Terminal Block OONO D-1410GP     |[Amazon](https://www.amazon.com/Position-Terminal-Distribution-OONO-D-1410GP/dp/B0DXF1GF9Q/ref=sr_1_1?crid=140OFKMTB914J&dib=eyJ2IjoiMSJ9.oyThY0ippJh2jpcbBoag45_Yy8PEQreSJWIoxRLGJHl0FzLTVwZoc02IwtBHRkfC0I7PYLYIWd6UbsHiUIrN3Pf6J1fmQ0WOdjOywU2Q4btVb0M56DmmQqjH2xy5OAeL.9n0Fz7UoURPFld0OI-_0_POLB5a_Wiq-rjM5o3Va7oI&dib_tag=se&keywords=16Amp%2BAC%2FDC%2B48V%2B2x12%2BPosition%2BTerminal%2BBlock%2BOONO%2BD-1410GP&qid=1753387584&s=electronics&sprefix=16amp%2Bac%2Fdc%2B48v%2B2x12%2Bposition%2Bterminal%2Bblock%2Boono%2Bd-1410gp%2Celectronics%2C157&sr=1-1&th=1)                                                                                                                                                                            |
| 2        | SoloGood 5V 5A (2s/3s/4s)        |[Amazon](https://www.amazon.com/SoloGood-Module-Quadcopter-Airplane-Servo/dp/B0C3GVGYDS/ref=sr_1_1?crid=130PU2TQP9VFF&dib=eyJ2IjoiMSJ9.5ilYenkdfQx0sH7IWq1Dsw.GcriRAsBaQcvL5bQL95L5kTVKu1i9MbWD0VondXRe0M&dib_tag=se&keywords=SoloGood+5V+5A+module+2s+3s+4s&qid=1753387657&s=electronics&sprefix=sologood+5v+5a+module+2s+3s+4s%2Celectronics%2C275&sr=1-1)                               |
| 1        | External UBEC 5V BEC Multi-Purpose Step-down Power Supply Module Full Shielding Antijamming for FPV Airplane (1PC 5V 7A)       |[Amazon](https://www.amazon.com/dp/B0D7MR48LB?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1)                               |
| 1        | Battery LiPo HOOVO 11.1V 3S 5200mAh 60C |[Amazon](https://www.amazon.com/HOOVO-11-1V-5200mAh-Softcase-Helicopter/dp/B0BWJH8G35/ref=sr_1_5?dib=eyJ2IjoiMSJ9.14IXf-IEW8YrQazHQ7fy_SYbRX19Y71vhVqgdLc_roy4_35L7F0517eY81ZP8PpX9AciCIoh2u6e5zViDL7hVdLpJ8hyiYrkcoIWxJ98IlKo82ZmZSACOFQtvBgSoSBZ8n6hxXRP72KHUtvgOP1Cir3AkjlaOk3ZJ9jagfyaJeRrSPA8HATfkxb5CISmEa4NIT98dzTQ4VUvqNvEvi6emUJW4g5I9VzpfQM1JT9MJwxvm3Y0C9B2HdZLFt-wsFTgGRfSCuZWWmdOYNCT_c7N6O5Y3tqUu8EIWLsFjBN5xiU.f-REaxpvTDZb27O-lM1suBBWJ6chVsI-lTcEvrHgPxE&dib_tag=se&keywords=HOOVO%2B11.1V%2B3s%2BLiPo%2BBattery%2B5200mAh%2B60c&qid=1753387686&sr=8-5&th=1)                                                                                                                                                                          |
| 1        | Chasis 4WD + servo S3003 |[Elecrow](https://www.elecrow.com/4wd-smart-car-robot-chassis-for-arduino-servo-steering.html)                                                                                                                             |
| Varios   | Jumper y cables                  |[Amazon](https://www.amazon.com/-/de/dp/B01EV70C78/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2A54IVO4KIECV&dib=eyJ2IjoiMSJ9.tjHxIQLJsk16_0YVtUGN6dGzV2wHYrdA_LNt2EBckEg2xcbQMpJP-tZhKHEuWRR-MW4OEUzxcuhDJWmZwkqQIS1B8R4KD9VPknZsY7K80ef8j7pG0HtHMmLqeqU7-A3Xsv5YYc2QReX4JbUyhsl0Q5pEnLjNCOn6odp-5DuUfT3mG8HtShQf_jbzv7-HTr3zvCq-5_0rhPXqgLbhG9gjPLVPjci9S5ODpgwZ0-cLdX4.BJ1rVbT8hocV1kpTSv17AsJTxlT80S-MM0gOof1DPbk&dib_tag=se&keywords=raspberry%2Bpi%2Bjumper%2Bwires&qid=1731244240&sprefix=raspberry%2Bpi%2Bjumper%2Bwire%2Caps%2C330&sr=8-3&th=1)|
| 1        | Cable 24 AWG PUDKLE (157ft)      |[Amazon](https://www.amazon.com/dp/B0DK57KRCT?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1)                                                                                                                                                                   |
| 2        | Logic Level Converter Bi-Directional Shifter Module 3.3V to 5V    |[Amazon](https://www.amazon.com/dp/B07CXMDJC2?ref=ppx_yo2ov_dt_b_fed_asin_title)   |
| 1        | Screw shield adaptador ESP-32    |[Mercado Libre](https://articulo.mercadolibre.com.mx/MLM-2162499429-screw-shield-adaptador-de-terminales-esp32-30-pines-_JM#origin%3Dshare%26sid%3Dshare)   |
| 1        | 6pcs DIN Rail Terminal Blocks    |[Amazon](https://www.amazon.com/dp/B0BQ6GWW3T?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1)   
| 3        | Ultrasonic sensors URM37V5.0     |[DigiKey](https://www.digikey.com/en/products/detail/dfrobot/SEN0001/6588449)    |
| 1        | USB to TTL Converter             |[Amazon](https://www.amazon.com/DSD-TECH-SH-U09C5-Converter-Support/dp/B07WX2DSVB/ref=sr_1_1_sspa?crid=2QX262TSU2971&dib=eyJ2IjoiMSJ9.D0amzFmzxb2ADgV4_ep2_cNsHofmse9FrT0i3YgPbkkxw9dDBUytrt0npuovbHnL_3S6v23XzdO_asu_QGvTb2Xjt8cJP9msCvWRym4dC-NQ5NTpSmg1KoBVbtpjXTKzSdeGcnmmJXYL0MKO4YnP0BkdedFIRCeQRcUuI0so7kzy4gRZetXyXEyAKVydX322o3dGYQZDO36bSsJFr7-PYeHAkOIlBLjA0B6oDqn0qCY.4Iuq8Gj72bw3DYdHWGSINCcQwrmvXEQQxcY40qAGySw&dib_tag=se&keywords=uart+to+usb.3v&qid=1754865582&sprefix=uart+to+usb.3%2Caps%2C240&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)    |

Estimated total cost ==> **$ 327.00 US dollars**.


|    Component         |   Function / Description                          |
|----------------------|---------------------------------------------------|
| Raspberry Pi 5       | Image processing and navigation logic             |
| ESP32                | Real-time servo control with PID algorithms and read sensors          |
| Camera               | Captures images for computer vision               |
| ARM37V5 (x3)         | Distance measurement for obstacle avoidance       |
| L298N Motor Driver   | Controls DC motors                                |
| DC Motor             | Robot movement                                    |
| Lipo Battery         | Portable power source                             |
| Voltage Regulator    | Stabilizes voltage for sensitive components       |
| UART Communication   | Link between Raspberry Pi and ESP32               |
| 2WD / 4WD Chassis    | Physical structure of the robot                   |
| Servo motor          | Controls steering direction                       | 


Software & Libraries Overview
|    Platform         |   Language / Frameworks          |   Key Functions / Roles                          |
|---------------------|----------------------------------|--------------------------------------------------|
| Raspberry Pi 5      | Python 3                         | Main control logic, image processing             |
|                     | OpenCV                           | Computer vision (line following, object tracking)|
|                     | pyserial                         | UART communication with ESP32                    |
|                     | numpy, imutils                   | Math operations, image transformations           |
| ESP32               | MicroPython                      | Lightweight firmware for real-time control       |
|                     | machine, time, ustruct           | Sensor reading, PWM generation, UART handling    |
|                     | PID function                     | Servo control                                    |


Workflow Table
|    Module           |    Function / Task                                      |
|---------------------|---------------------------------------------------------|
| Raspberry Pi 5      | Captures image via camera                               |
|                     | Processes image using OpenCV (color)                    |
|                     | Determines direction.                                   |
|                     | Sends commands to ESP32 via UART                        |
| ESP32               | Receives commands from Raspberry Pi                     |
|                     | Reads ultrasonic sensor data                            |
|                     | Applies PID control to maintain safe distance           |
|                     | Controls motors and servo using PWM                     |



[Menu](#Contents)
___



## Mobility Management.
====

**Design Objectives**

The mobility system was designed to meet the following goals:

- **Precision**: Achieve controlled movement and accurate steering.
- **Stability**: Maintain balance and traction across varied surfaces.
- **Mechanical Efficiency**: Use gear ratios to optimize torque and speed.
- **Adaptability**: Respond effectively to terrain changes and obstacles.


**Gear Transmission**: Power is delivered from the motors to the wheels through a custom gear system. Gear ratios were selected to enhance torque for low-speed control and obstacle negotiation.

Mobility is a key factor in robotic performance, especially in competitive environments where precision, stability, and adaptability are essential. This document outlines the mechanical and software strategies used to manage the robot's mobility, featuring a gear-based transmission system and directional control via a servomotor.

<img width="886" height="300" alt="image" src="https://github.com/user-attachments/assets/eefbba07-8c55-4ca0-945b-d09acaefd093" />

<img width="841" height="316" alt="image" src="https://github.com/user-attachments/assets/7f6f4bb1-04b4-4737-a7f4-04a1430fb224" />



The gear transmission is a mechanical system that allows for the modification of angular velocity and torque between two connected shafts. This is achieved by coupling two gears: a driving gear (coupled to the motor) and a driven gear (coupled to the load or wheel).

Based on the previous terms, we use them in the robot as follows:

1. For the free challenge, it is required that the robot has more speed than torque, which is why the driven gear has 54 teeth in relation to the driving gear of 32. If we apply the principle of conservation of mechanical power,
  
   where:  RT =   driven gear teeth / driving gear teeth = 54 / 32 = **1.68**

   
2. For the obstacle challenge, it is required that the robot moves slowly and with more torque, resulting in the driven gear for this particular challenge having 32 teeth and the driving gear having 54, so that by applying the principle of conservation of power, a decrease in speed is obtained, but torque increases in the following proportion:


   where:  RT =   driven gear teeth / driving gear teeth = 32 / 54 = **0.59**


The motor is controlled using the pulse width modulation technique. Pulse Width Modulation (PWM) is a widely used technique for controlling the speed of DC motors by adjusting the effective voltage applied to the motor terminals. Instead of varying the actual supply voltage, PWM rapidly switches the motor’s power on and off at a fixed frequency, modulating the duration of the “on” time within each cycle—this is known as the duty cycle. The motor’s speed is directly influenced by the duty cycle of the PWM signal. A higher duty cycle means the motor receives power for a greater portion of each cycle, resulting in a higher average voltage and increased rotational speed. Conversely, a lower duty cycle reduces the average voltage and slows the motor down. The configuration parameters are shown below:


**These are the parameters defined for the open-category challenge:**


enable = PWM(Pin(21), freq=1000)        # Motor PWM enable

enable.duty_u16(35000)                  # Set duty cycle to ~53.4%



- Pin(21): Refers to GPIO pin 21 on the microcontroller (ESP32). This pin is physically connected to the motor driver’s (L298N) enable input, which expects a PWM signal.
- PWM(...): Initializes a PWM object on that pin.
- freq=1000: Sets the PWM frequency to 1000 Hz (1 kHz), meaning the signal completes 1000 cycles per second.
- duty_u16(...): Sets the duty cycle using a 16-bit value (range: 0 to 65535).
- 35000: Represents the “on” time of the PWM signal. The duty cycle percentage is:
  Duty Cycle(%) = (35000 / 65535) * 100                **approx 53.4\%**
- This means the signal is high (ON) for 53.4%.
- Average Voltage: The motor receives approximately 53.4% of the supply voltage. If V = 11.1 V, then:
  V = 11.1V * 0.534      **approx 6V**


Based on the measured values and the technical specifications provided by the manufacturer, the following results are obtained:

| Parameter             | Measured Value | Unit       |
|----------------------|----------------|------------|
| No-load Speed         | 646            | RPM        |
| No-load Current       | 0.1            | A          |
| Rated Torque          | 0.23           | Kg-cm      |
| Power                 | 1.5            | W          |
| Load Speed            | 516            | RPM        |
| Load Current          | 0.8            |  A         |
| Stall Torque          | 2              | Kg-cm      |
| Stall Current         | 2              | A          |
| Operating Voltage     | 6.0            | V          |

[Reference](https://www.elecrow.com/4wd-smart-car-robot-chassis-for-arduino-servo-steering.html)


**The following parameters were defined for the obstacle challenge:**

- 26000: Represents the “on” time of the PWM signal. The duty cycle percentage is:
  Duty Cycle(%) = (26000 / 65535) * 100                **approx 39.6\%**
- This means the signal is high (ON) for 39.6%.
- Average Voltage: The motor receives approximately 39.6% of the supply voltage. If V = 11.1 V, then:
  V = 11.1V * 0.396      **approx 4.39V**


Based on the measured values and the technical specifications provided by the manufacturer, the following results are obtained:

| Parameter             | Measured Value | Unit       |
|----------------------|----------------|------------|
| No-load Speed         | 472            | RPM        |
| No-load Current       | 0.073          | A          |
| Rated Torque          | 0.263          | Kg-cm      |
| Power                 | 1.0            | W          |
| Load Speed            | 377            | RPM        |
| Load Current          | 0.58           |  A         |
| Stall Torque          | 2              | Kg-cm      |
| Stall Current         | 1.46           | A          |
| Operating Voltage     | 4.39           | V          |

[Reference](https://www.elecrow.com/4wd-smart-car-robot-chassis-for-arduino-servo-steering.html)


**Directional Control**: A high-precision servomotor is used to steer the front axle, allowing for smooth and responsive turns. This setup mimics real-world vehicle steering and improves maneuverability in tight spaces.

<img width="941" height="372" alt="image" src="https://github.com/user-attachments/assets/5a6086d7-6189-4b04-94b4-430630bc0873" />

<img width="743" height="414" alt="image" src="https://github.com/user-attachments/assets/e593d6eb-0339-429c-9243-569fbea22d5e" />

<img width="1010" height="271" alt="image" src="https://github.com/user-attachments/assets/add06f32-cd43-4ca6-af2d-0291b82927d2" />



The foundation of our chassis design is based on a steering configuration known as the parallel steering model, in which both front wheels turn at the same angle when steering input is applied. This approach, while mechanically straightforward, provides a reliable baseline for mobile robot steering systems—especially when simplicity, symmetry, and ease of implementation are key priorities.


<img width="541" height="250" alt="image" src="https://github.com/user-attachments/assets/5f82ad7a-f967-4f60-8227-f051eb56edba" />

In short, parallel steering was chosen because it strikes a balance between functionality and feasibility. It enables reliable performance while keeping the mechanical and computational demands accessible—perfect for STEM education, prototyping, and early-stage competition builds.

The selection was based mainly on the following reasons:

1. Mechanical Simplicity
- The parallel steering model allows both front wheels to turn at the same angle using a single servo or mirrored linkage system.
- This reduces the number of moving parts and avoids the need for complex geometry or differential steering mechanisms.
2. Ease of Control
- From a programming standpoint, controlling a single angle for both wheels is straightforward.
- It simplifies PID tuning, sensor feedback loops, and integration with basic autonomous navigation systems.
3. Modular Compatibility
- Many commercial chassis kits (like those using MG996R servos or JGA25-370 motors) are designed with parallel steering in mind.
- This makes it easier to integrate with off-the-shelf components and adapt to different platforms.
4. Symmetry and Predictability
- Parallel steering provides predictable turning behavior, which is useful for line-following, maze-solving, or path planning in competition environments.
- It also simplifies documentation, calibration, and debugging.



**Motor and Servo Specifications**

| Parameter         | JGA25-370 Gear Motor (12V)           | MG996 Servo Motor (6V)             |
|------------------|--------------------------------------|------------------------------------|
| **Operating Voltage** | 6V / 12V / 24V DC                    | 4.8V – 6V DC                        |
| **No-Load Speed**     | 12 – 1350 rpm (depends on gear ratio) | 0.14 s/60° (≈ 428°/s)              |
| **Rated Speed**       | 9 – 1000 rpm                        | Controlled via PWM (0°–180°)       |
| **Stall Torque**      | Up to 9 kg·cm (gear ratio dependent) | 11 kg·cm                            |
| **Rated Torque**      | 0.6 – 9 kg·cm                        | ~2.5 – 9.4 kg·cm (typical range)   |
| **Power Output**      | 1.6W – 3W                            | ~2.5W (estimated)                  |
| **Current Draw**      | ≤0.25A rated / ≤3A stall             | ~500mA running / 2.5A stall        |
| **Rotation Range**    | Continuous                          | 0° to 180°                         |
| **Control Method**    | PWM + gear ratio                    | PWM signal (50Hz, 1–2ms pulse)     |

**JGA25-370 Motor Specifications by Voltage**

| Voltage (V) | No-load Speed (rpm) | Rated Torque (kg·cm) | Power (W) | Load Speed (rpm) | Load Current (A) | Stall Torque (kg·cm) |
|-------------|----------------------|------------------------|-----------|-------------------|-------------------|------------------------|
| 3V          | 323                  | 0.18                   | 0.75      | 258               | 0.4               | 1.4                    |
| 6V          | 646                  | 0.23                   | 1.5       | 516               | 0.8               | 2.0                    |
| 12V         | 592                  | 0.23                   | 2.3       | 475               | 0.6               | 2.0                    |
| 24V         | 409                  | 0.15                   | 1.0       | 347               | 0.5               | 1.3                    |

>  **Technical Notes**:
> - Best performance observed at **12V**, offering solid torque and peak power.
> - Stall torque values are useful for defining load limits and implementing software protection.
> - Ideal for traction, drive systems, or actuator applications with PWM control.



**Chassis Adaptation and Structural Enhancements**: 

A commercial chassis kit was initially acquired as the mechanical foundation for the robot. However, significant structural and functional improvements were implemented to optimize device integration and system stability.
Custom mounting platforms were designed and fabricated to securely accommodate key components such as the ESP32 microcontroller, the Raspberry Pi 5 single-board computer, the camera module, and the sensor array. These modifications involved redesigning the original base plates to ensure precise alignment, vibration damping, and thermal clearance for high-performance operation.
The updated design also includes reinforced brackets and modular supports that facilitate rapid maintenance and component replacement during competition. These enhancements substantially diverge from the original kit layout, resulting in a more robust, competition-ready architecture.
The following technical drawings illustrate the custom adaptations made to the chassis, highlighting the engineering rationale behind each modification and its impact on system performance. The most critical structural adaptations are presented below. These modifications were implemented to enhance component stability, optimize spatial distribution, and improve overall system integration.
Full CAD models and detailed design files can be found in the  folder, including all custom mounts, sensor brackets, and revised base plates. These designs reflect substantial changes to the original kit configuration, tailored to meet the specific demands of the obstacle and open-category challenges.

**Sensors base.**   
![](models/base_urm37_v7.JPG)

**Camera base.**
![](models/base_camera2_V2.JPG)
![](models/base_camera_v2.JPG)
![](models/tapa_camera.JPG)

**Main base.**
![](models/base_principal_V6.JPG)





**Software Integration**

- **Motor Control**: PWM signals regulate motor speed, while gear ratios provide mechanical tuning. The servomotor is controlled via angle commands for directional adjustments.
- **Error Handling**: The system includes routines to detect gear misalignment, servo overload, or terrain anomalies, triggering corrective actions when needed.

![GeneralProgramOpen](https://github.com/user-attachments/assets/3c89ec7e-4f5e-468b-badf-5f88ac1e12d4)

![get_data](https://github.com/user-attachments/assets/9a877113-cd5c-475c-989b-8628b9331b69)

![get_distance](https://github.com/user-attachments/assets/ea045c30-431b-46f1-bb69-cf1e2c8eb504)

![turn_servo](https://github.com/user-attachments/assets/b4824778-0cdc-4403-8423-9ba04be3e97c)

![turn_robot](https://github.com/user-attachments/assets/a11d5da2-e261-4628-8072-73cda4d6c313)

![pid](https://github.com/user-attachments/assets/e41df90c-652f-4877-9b12-4f1181881fed)






**Performance Evaluation**

Mobility was tested under various conditions:

- **Obstacle Navigation**: The robot demonstrated reliable steering and movement over uneven surfaces and around barriers.
- **Turning Radius**: The servomotor-based steering allowed for tighter turns compared to differential drive systems.
- **Load Testing**: Gear ratios and servo torque were validated under different payloads to ensure consistent performance.
- **Energy Efficiency**: Power consumption was monitored to balance torque output, steering precision, and battery endurance

---

**Chassis Selection and Custom Adaptations**

This project utilizes a commercial chassis with **custom structural own modifications** to support advanced robotics integration. The chassis has been adapted to include:

- **Sensor mounting base** – for ultrasonic sensors
- **Connector interface base** – for clean wiring and modular component swaps
- **ESP32 microcontroller base** – optimized for MicroPython deployment and GPIO access
- **Camera module base** – compatible with vision systems
- **Raspberry Pi 5 integration base** – for high-level processing, remote monitoring, and AI tasks

These adaptations ensure modularity, scalability, and ease of maintenance during competition and development phases.

A commercial chassis was selected to optimize structural integrity, motor compatibility, and sensor placement for the mobile robot platform. Below are its key specifications:

| Feature                  | Specification                          |
|--------------------------|----------------------------------------|
| **Material**             | Metal chassis / ABS plastic           |
| **Dimensions (L×W×H)**   | 248 mm × 146 mm × 70 mm                |
| **Wheel Type**           | 2WD with rubber tires (65 mm diameter) |
| **Motor Mounts**         | Compatible with JGA25-370 gear motors  |
| **Servo Mounts**         | Integrated brackets for MG996 servo    |
| **Sensor Slots**         | Front and side slots for ultrasonic sensors |
| **Battery Compartment**  | Supports 2S/3S Battery LiPo HOOVO 11.1V 3S 5200m    |
| **Weight Capacity**      | ~1.5 kg payload                        |
| **Shock Absorption**     | Rubber dampers included                |

>  **Design Rationale**:
> - Chosen for its modularity and ease of integration with ESP32 and Raspberry 5.
> - Provides stable base for F1-style mobility and sensor calibration.
> - Lightweight yet durable, ideal for competition and field testing.
>

**Engineering Principles Applied**

The design and implementation are grounded in core engineering concepts:

- **Angular velocity**: Used to calculate linear displacement from motor rpm.
- **Torque**: Determines traction force and load capacity.
- **Power**: Guides battery selection and motor efficiency.
- **Mass distribution**: Ensures stability and maneuverability.

**3D Printed Components**

Complementary 3D-printed parts used to enhance the commercial chassis are included in the `models/` folder located at the top level of this repository.

These components include:
- **Sensor mounts** (ultrasonic)
- **Battery holders**
- **Structural reinforcements** and expansion adapters

>  All files are provided in `.STL` format and are ready for slicing and printing. Designed for compatibility with standard FDM printers and PLA/ABS materials.

Feel free to modify or remix these models to suit your specific configuration. Contributions and improvements are welcome!


[Menu](#Contents)
___

## Power and Sensor Management.
====

Efficient energy and sensor management are essential for reliable vehicle performance. This section outlines the power strategy, sensor selection, and system integration used in the robot.
Three sensors were used to provide the microcontroller (ESP32) with the necessary information to navigate the track and overcome various challenges. One sensor is mounted on the right side of the vehicle to work in conjunction with the PID controller, maintaining a specific distance from the wall. Another sensor is placed on the left side, performing the same function on the opposite side. A third sensor is positioned facing forward to monitor when the robot approaches the front wall.

**Current Consumption Analysis – Robotic System**

| Component               | Quantity | Voltage (V) | Current per unit (A) | Total current (A) | Max total current (A) |
|------------------------|----------|-------------|-----------------------|--------------------|------------------------|
| JGA25-370 Motor        | 1        | 11          | 0.6                   | 0.6                | 0.6                    |
| MG996R Servo           | 1        | 5.0         | 0.5                   | 0.5                | 1.0                    |
| Raspberry Pi 5         | 1        | 5           | 1.2                   | 1.2                | 4.5                    |
| ESP32                  | 1        | 5           | 0.08                  | 0.08               | 0.08                  |
| URM37V5 Sensor         | 3        | 5           | 0.02                  | 0.06               | 0.06                   |
| L298N (logic circuit)  | 1        | 5           | 0.05                  | 0.05               | 0.05                   |
| **Estimated Total**    | —        | —           | —                     | **2.49 A**         | **6.29 A**             |

**Power Supply Strategy**

The power system is designed to support motors, servos, microcontrollers, and sensors simultaneously. Key considerations includes two challenges, each powered by a different voltage source.
For the open challenge and the obstacle challenge, the system is powered by a battery that supplies 5200 mA.
Detailed battery specifications are provided below

- **Battery type**  
  - Battery LiPo HOOVO 11.1V 3S 5200mAh 60C

- **Power regulation**  
  - Buck converters or dedicated power rails to prevent voltage drops and protect sensitive components

**Sensor Selection and Justification**
Three sensors were selected to provide the robot with positioning information on the track.
They were mounted on the front of the robot: one on the right side, one on the left side, and one in the center.
This configuration allows the robot to detect lateral boundaries and maintain alignment during navigation.

The side-mounted sensors provide the system with distance measurements between the robot and the lateral walls.
A PID control algorithm was implemented to maintain a consistent, predefined distance from these walls during navigation.
The center sensor supplies data regarding the robot’s proximity to the front wall, enabling forward obstacle detection and alignment.
Each sensor contributes to navigation, obstacle detection, or environmental awareness:

| Sensor       | Purpose                     | Protocol | Power Notes         |
|--------------|-----------------------------|----------|----------------------|
| 3.- URM37V5.0    | Distance measurement        | Digital  | Low consumption      |


**System Integration Overview**

A wiring diagram and bill of materials (BOM) will be included to illustrate:

- Power distribution across all components.
- Voltage regulation.
- Microcontroller pin mapping.
- Sensor interconnections and shielding.


[Menu](#Contents)
___

## Obstacle management.
====

This system pairs a Raspberry Pi 5 vision producer with an ESP32 motion controller for WRO 2025. On the Pi 5, WRO_headless.py captures frames via Picamera2, crops a horizontal ROI to focus compute, converts to HSV, and segments red (two hue bands for wraparound) and green. A 5×5 morphological opening suppresses noise; external contours are extracted and the largest blobs are measured. Detections below a minimum area are ignored; exceeding a “critical” area flags an immediate pillar. The Pi compares critical red vs green and sends a single byte—'R', 'G', or 'C'—over UART at 115200 baud. The ESP32 (MicroPython) reads this on UART2 (TX=GPIO17, RX=GPIO16), drives motors with LEDC PWM, and positions the steering servo at calibrated LEFT/CENTER/RIGHT bounds. Ultrasonic distances (HC-SR04 style via time_pulse_us) refresh continuously. A wall-following PID (tunable KP/KI/KD, DT) steers each cycle; on 'R'/'G', a lane-change primitive boosts speed, steers diagonally with a minimum hold, requires a lateral distance delta or times out, then counter-turns and recovers before PID resumes. A debounced corner routine triggers when front distance stays below threshold. Calibrate HSV, ROI, area gates, PID gains, and maneuver timings.
The connection diagram is shown in section schemes.
The source code is in section src.


[Menu](#Contents)
___


## Work log.
====

may 2, 25

start of assembling the robot prototype with lego ev3 to begin code testing

may 3-8, 25

program testing period using ev3.

may 9, 25

start of assembling the final robot prototype

may 12, 25

completion of the final prototype assembly and beginning of test with it.

may 13, 25

integration and verification of l298n driver for dc motor control.

may 19. 25

evaluation of the vl53l0x distance sensor for short-range measurements

may 21, 2025

instalation and testing of the servo motor for steering control on the robotic plataforma.

may 26, 2025

initial test of pulse width modulation(pwm) por speed control.

may 27, 2025

integration of pwm control with the l298n driver and synchronization with the servo motor.

june 2, 2025

inclusion of the vl53l0x sensor into the main program for continuous distance measurement.

june 10, 2025

testing and calibration of the vl53l0x sensor and the servomotor on the robot's base structure.

june 16, 2025

calibration and adjustment of program parameters associated with the tcs34725 sensor to optimize color detection.

june 23, 2025

testing the main program with the vl53l0x sensor and integrating functions for measuring distance and pid settings.

june 30, 2025

the first program was made with the tcs34725 sensor to detect the blue and orange colors of the track to determine the robot0s course.

july 1, 2025

program with the tcs34725 sensor to detect blue and orange strippes. The sensor does not provide adequate measurements at the speed used for the challenge

july 7, 2025

the vl53l0x sensor was replaces with an ultrasonic sensor due to accuracy issues. a program was created with the ultrasonic sensor to measure distances and verify the sensors.

july 11, 2025

Hitechnic: This sensor was used to detect turns and the section of the track, the blue and orange stripes, so that the robot knew where to stop.in the end, due to the robot´s speed, the strips could not be detected and it was not used.

july 14, 2025

the part used as the main base, where the raspbery pi 5 and esp32 are mounted, was designed in SolidWorks, it was printed ande placed on the robot´s structure. File name: base_principal_v6.stl

july 15, 2025

The part used as the base for the 16amp ac/dc 48v 2x12 position terminal block distribution module connector was designed, printed, and placed on the robot frame. File name: base_conector_v3.stl
The vl53l0x sensor was completely discarted due to reading errors on black surfaces.

july 16, 2025

the part used as a complementary base for the raspbery pi 5 , was designed in SolidWorks, it was printed ande placed on the robot´s structure. File name: base_pi_5_v5.stl

july 17, 2025

measurements and calibrations of the servomotor to detect the angles requeried to control the robot for turns and straight forward motion.

July 18, 2025

the part used as the main base por mounting the camera, was designed in SolidWorks, it was printed ande placed on the robot´s structure. File name: base_camera_v2.stl.
The pid was tuned to 30000 and 50000 for testing.

July 19,2025

The part used as a complementary bose for the camera was designed n solidworks, printed, and placed on the robot structure.
File name: base-Camera-U2. STL.

July 20,2025

The part used as the camera cover was designed, printed and placed on the robot structure. File rame: tapa-Camera. STL

July 27,2025

The Pi5 camera was contigured for continuos capture and manual parameter control (150, exposure, resolution). Cu2 was integrated for the complete acquisition → Processing→ visualization workflow. The Urm37 cables were soldered to integrate the sensors into the robot.

July 28. 2025

Testing began with the Urm37 sensor to verity its effectiveness, UART conection tests for the Pi5, and the start button was integrated into the robot.

July 30, 2025

The part used as a base to support the three Ultrasonic sensors. was designed, printed and placed on the robot's structue.
file name: base_urm37_v7.STL

July 31,2025

Measurements of the robot's positions on the track, Based on this, a program was created to determinate the robot's position.

Aug 01, 2025

Rotation reading with Mpu6050. gyro-90.
Formulas were used to perform PID calculations using the discrete method.

Aug 2, 2025

The part used as a base to support the robot was designed in solidworks and printed. File name: base_robot_v2.STL

Aug 4, 2025

Testing began with the Gy-521 sensor. It worked well, but when the motor was ruming it stopped working.

Aug 7, 2025

Testing began with the as5600 Encoder sensor with a magnet, wich works usng the Hall method.
It did not wons as expected and was discontinued.

Aug 08,2025

The pid tuning was completed the mpu6050 sensor was tested But The Decision Was Made to Control the rotation, with the ultrasonic, sensor On The Front of The robot.
The bts 7960 driver was added.

Aug 10, 2025

Challenge 1 testing was completed. A magnetometer was included to determinate which direction the robot would start in. Due to poor measurements, lt was discarted.

Aug 15,2025

Feal-time mage capture, processing, and analysis tests were performed. Color conversion (RGB) and basic segmentation functions were implemented. Cu2 was integrated into the rasperry PI5 to validate performance under real-world conditions for detecting red and green blocks.

Aug 18, 2025

Numpy: used for image matrix manipulation, histogram calculations, and vectorized operations. Processing routines were optimized using multidimentional arrays, reducing execution time in repetitive tasks. Use cases were documented in inage analysis scripts.

Aug 23, 2025

Pid control adjustments for robot ravigation.

Aug 24-30, 2025

Trial perod for both challenges

Aug 30, 2025

The servomator broke down, it was changed and recalibrated


[Menu](#Contents)
___

## References.
====

[1] Alouache A., Wu Q., "Genetic Algorithms for Trajectory Tracking of Mobile Robot Based on PID Controller". 2018 IEEE 14th International Conference on Intelligent Computer Communication and Processing (ICCP). DOI: 10.1109/ICCP.2018.8516587. IEEE. ISBN:978-1-5386-8446-7.

[2] Qi Z., Yang H., Li M., Li J., "Research on Fractional Order PID Controller in Servo Control System". 2019 IEEE 3rd Conference on Energy Internet and Energy System Integration (EI2). DOI: 10.1109/EI247390.2019.9062032. IEEE. ISBN:978-1-7281-3138-2.

[3] Luo Z., Li W., "Tracking of Mobile Robot Expert PID Controller Design and Simulation". 2014 International Symposium on Computer, Consumer and Control. IEEE.  2014 International Symposium on Computer, Consumer and Control. DOI: 10.1109/IS3C.2014.154. Electronic ISBN:978-1-4799-5277-9. 

[4] Schtchikov Y., Sokolova S., "Technical Vision for Object Recognition", 2024 International Conference on Industrial Engineering, Applications and Manufacturing (ICIEAM), DOI: 10.1109/ICIEAM60818.2024.10553791, Electronic ISBN:979-8-3503-9501-3.


[Menu](#Contents)
___

