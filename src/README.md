Control software
====

This directory contain code for control software which is used by the vehicle to participate in the competition and which was developed by the participants.

## Version History

### v1.0.0 – Initial Release
- Basic sensor integration (vl53l0x) with ESP32 using MicroPython
- Modular code structure with functions.
- Basic error handling.

### v1.1.0 – Sensor Expansion and PID control.
- Added support for URM37 sensors.
- Improved abstraction and reusable modules.
- Implemented PID control for steering.
- Real-time PID parameter adjustment.
- Improved trajectory stability and response time.

### v1.2.0 – Final release free challenge.
- Improvements were added to the startup routine to detect which direction to turn.

### v2.1.0 – Final release challenge obstacles.
- This code is for the ESP-32 in charge of carrying out the obstacle course, it communicates via serial with the Raspberry Pi 5,   receives commands to control the robot, and contains a PID to navigate the track.
