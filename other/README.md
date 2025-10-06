
**Work Log.**
====


**February 3 – May 2, 2025:** Team Formation & Initial Prototyping

Objectives:
- Establish the core development team for the 2025 WRO season Future Engineers.
- Begin iterative testing of mechanical and software subsystems using LEGO EV3 platform.

Activities:
- Team onboarding and role assignment (mechanical, programming, documentation).
- Assembly of preliminary EV3-based robot for concept validation.
- Initial design trials:
  - Chassis stability and modularity
  - Sensor placement and cable management
- First code experiments:
  - Motor control routines (EV3 Large/Medium motors)
  - Sensor polling (ultrasonic, color, gyro)
  - Basic task automation (line following, object detection)

Outcomes:
- Functional prototype for early-stage testing
- Identification of design constraints and improvement areas

**May 3–8, 2025:** EV3 Program Testing

Focus
Software validation and refinement for LEGO EV3 platform using MicroPython.

Activities
- Executed structured tests on core program modules:
  - Motor control routines (start/stop, speed modulation)
  - Sensor polling and data handling (ultrasonic, color)
- Verified timing consistency and response accuracy under varying conditions.
- Logged performance metrics and anomalies for future optimization.
- Updated codebase with modular improvements and inline documentation.

Outcomes
- Confirmed baseline functionality of EV3 control algorithms.
- Identified edge cases requiring exception handling.

All tests conducted on LEGO EV3 hardware using MicroPython. Results documented for reproducibility and future integration.

**May 9, 2025:** Start of Final Robot Prototype Assembly

Objective
Initiate the physical construction of the final robot prototype for the 2025 WRO challenge, integrating validated subsystems and transitioning from experimental builds to competition grade architecture.

Activities
- Selected final components based on prior testing:
  - Reinforced chassis elements and modular mounts
- Assembled mechanical structure:
  - Optimized layout for sensor visibility and cable management
  - Reinforced motor mounts for stability under dynamic loads
  - Integrated modular attachments for task-specific tools
- Began integration of software modules:
  - Motor control and sensor polling routines
  - Task automation scripts adapted to final layout
  - Safety checks and exception handling

Outcomes
- Physical assembly of the final robot prototype initiated
- Mechanical and electrical subsystems aligned with competition requirements
- Codebase adapted to final hardware configuration
- Documentation updated for traceability and sponsor review


**May 12, 2025:**

completion of the final prototype assembly and beginning of test with it.

**May 13, 2025:**

integration and verification of l298n driver for dc motor control.

**May 19, 2025:**

evaluation of the vl53l0x distance sensor for short-range measurements

**May 21, 2025:**

instalation and testing of the servo motor for steering control on the robotic plataforma.

**May 26, 2025:**

initial test of pulse width modulation(pwm) por speed control.

**May 27, 2025:**

integration of pwm control with the l298n driver and synchronization with the servo motor.

**June 2, 2025:**

inclusion of the vl53l0x sensor into the main program for continuous distance measurement.


**June 10, 2025:**

testing and calibration of the vl53l0x sensor and the servomotor on the robot's base structure.

**June 16, 2025:**

calibration and adjustment of program parameters associated with the tcs34725 sensor to optimize color detection.

**June 23, 2025:**

testing the main program with the vl53l0x sensor and integrating functions for measuring distance and pid settings.

**June 30, 2025:**

the first program was made with the tcs34725 sensor to detect the blue and orange colors of the track to determine the robot0s course.

**July 1, 2025:**

program with the tcs34725 sensor to detect blue and orange strippes. The sensor does not provide adequate measurements at the speed used for the challenge

**July 7, 2025:**

the vl53l0x sensor was replaces with an ultrasonic sensor due to accuracy issues. a program was created with the ultrasonic sensor to measure distances and verify the sensors.

**July 11, 2025:**

Hitechnic: This sensor was used to detect turns and the section of the track, the blue and orange stripes, so that the robot knew where to stop.in the end, due to the robot´s speed, the strips could not be detected and it was not used.

**July 14, 2025:**

the part used as the main base, where the raspbery pi 5 and esp32 are mounted, was designed in SolidWorks, it was printed ande placed on the robot´s structure. File name: base_principal_v6.stl

**July 15, 2025:**

The part used as the base for the 16amp ac/dc 48v 2x12 position terminal block distribution module connector was designed, printed, and placed on the robot frame. File name: base_conector_v3.stl The vl53l0x sensor was completely discarted due to reading errors on black surfaces.

**July 16, 2025:**

the part used as a complementary base for the raspbery pi 5 , was designed in SolidWorks, it was printed ande placed on the robot´s structure. File name: base_pi_5_v5.stl

**July 17, 2025:**

measurements and calibrations of the servomotor to detect the angles requeried to control the robot for turns and straight forward motion.

**July 18, 2025:**

the part used as the main base por mounting the camera, was designed in SolidWorks, it was printed ande placed on the robot´s structure. File name: base_camera_v2.stl. The pid was tuned to 30000 and 50000 for testing.

**July 19, 2025:**

The part used as a complementary bose for the camera was designed n solidworks, printed, and placed on the robot structure. File name: base-Camera-U2. STL.

**July 20, 2025:**

The part used as the camera cover was designed, printed and placed on the robot structure. File rame: tapa-Camera. STL

**July 27, 2025:**

The Pi5 camera was contigured for continuos capture and manual parameter control (150, exposure, resolution). Cu2 was integrated for the complete acquisition → Processing→ visualization workflow. The Urm37 cables were soldered to integrate the sensors into the robot.

**July 28, 2025:**

Testing began with the Urm37 sensor to verity its effectiveness, UART conection tests for the Pi5, and the start button was integrated into the robot.

**July 30, 2025:**

The part used as a base to support the three Ultrasonic sensors. was designed, printed and placed on the robot's structue. file name: base_urm37_v7.STL

**July 31, 2025:**

Measurements of the robot's positions on the track, Based on this, a program was created to determinate the robot's position.

**August 1, 2025:**

Rotation reading with Mpu6050. gyro-90. Formulas were used to perform PID calculations using the discrete method.

**August 2, 2025:**

The part used as a base to support the robot was designed in solidworks and printed. File name: base_robot_v2.STL

**August 4, 2025:**

Testing began with the Gy-521 sensor. It worked well, but when the motor was ruming it stopped working.

**August 7, 2025:**

Testing began with the as5600 Encoder sensor with a magnet, wich works usng the Hall method. It did not wons as expected and was discontinued.

**August 8, 2025:**

The pid tuning was completed the mpu6050 sensor was tested But The Decision Was Made to Control the rotation, with the ultrasonic, sensor On The Front of The robot. The bts 7960 driver was added.

**August 10, 2025:**

Challenge 1 testing was completed. A magnetometer was included to determinate which direction the robot would start in. Due to poor measurements, lt was discarted.

**August 15, 2025:**

Feal-time mage capture, processing, and analysis tests were performed. Color conversion (RGB) and basic segmentation functions were implemented. Cu2 was integrated into the rasperry PI5 to validate performance under real-world conditions for detecting red and green blocks.

**August 18, 2025:**

Numpy: used for image matrix manipulation, histogram calculations, and vectorized operations. Processing routines were optimized using multidimentional arrays, reducing execution time in repetitive tasks. Use cases were documented in inage analysis scripts.

**August 23, 2025:**

Pid control adjustments for robot ravigation.

**August 24-30, 2025:**

Trial perod for both challenges

**August 30, 2025:**

The servomator broke down, it was changed and recalibrated

[Menu](#Contents)
___
