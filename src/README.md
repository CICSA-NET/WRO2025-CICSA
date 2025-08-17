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

