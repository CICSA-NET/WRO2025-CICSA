Control software
====

This directory contain code for control software which is used by the vehicle to participate in the competition and which was developed by the participants.

## Version History

### v1.0.0 – Initial Release
- Basic sensor integration (vl53l0x) with ESP32 using MicroPython
- Modular code structure with functions.
- Basic error handling.

### v1.1.0 – Sensor Expansion
- Added support for URM37 and TOF10120 sensors
- Implemented Kalman filtering for noisy data
- Improved abstraction and reusable modules

### v1.2.0 – OTA Programming & Diagnostics
- Enabled OTA updates via Wi-Fi (MicroPython + Arduino IDE)
- Added diagnostic logging and fault recovery routines
- Markdown documentation for setup and usage

### v1.3.0 – F1 Mobile Robot Integration
- Full integration with mobile robot platform
- Real-time sensor fusion and motor control
- Sponsorship-ready documentation and visuals

### v1.4.0 – Web Interface & Remote Monitoring
- Basic web dashboard for sensor data visualization
- Remote control via HTTP requests
- Optimized memory usage and performance
