Control software
====

This directory contain code for control software which is used by the vehicle to participate in the competition and which was developed by the participants.

## Version History

### pid_esp.py – First version of the code (ESP-32).
- Basic sensor integration (vl53l0x) with ESP32 using MicroPython
- Modular code structure with functions.
- Basic error handling.

### mainDef15-08_V1.1.0.py – Sensor Expansion and PID control (ESP-32).
- Added support for URM37 sensors.
- Improved abstraction and reusable modules.
- Implemented PID control for steering.
- Real-time PID parameter adjustment.
- Improved trajectory stability and response time.

### main_10_09_25_V1.2.0.py – Final release free challenge (ESP-32).
- Improvements were added to the startup routine to detect which direction to turn.

### main_10_09_25_V1.3.0.py – Final release free challenge (ESP-32).
- Final Program with comments.


### main_16_09-25_V2.1.0 – Final release challenge obstacles (ESP-32).
- This code is for the ESP-32 in charge of carrying out the obstacle course, it communicates via serial with the Raspberry Pi 5,   receives commands to control the robot, and contains a PID to navigate the track.

### main_16-09-25_V2.2.0.py – Final release challenge obstacles (ESP-32).
- Final Program with comments.

### main_16-09-25_V3.1.0.py – Final release challenge obstacles (Raspberry Pi 5).
- This is the main code installed on the Raspberry Pi 5, which contains the cv2, numpy, serial, time, and picamera2 libraries. To detect obstacles, it communicates with the ESP-32 to control the robot.


### main_16-09-25_V3.2.0.py – Final release challenge obstacles (Raspberry Pi 5).
- Final Program with comments.



[Menu](https://github.com/CICSA-NET/WRO2025-CICSA/blob/main/README.md)
___
