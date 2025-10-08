
**Digital Engineering Logbook.**
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


**May 12, 2025:** Completion of Final Prototype Assembly and Start of Testing
Objective
Finalize the physical assembly of the competition grade robot and initiate functional testing.
Activities
- 	Completed mechanical and electrical integration of validated subsystems
- 	Verified structural integrity and cable routing
- 	Initiated basic movement and sensor response tests
Outcomes
- 	Final prototype fully assembled
- 	Testing phase officially launched

**May 13, 2025:** Integration of L298N Driver for DC Motor Control
Objective
Enable precise motor control using the L298N H bridge driver.
Activities
- 	Connected L298N to motor and microcontroller
- 	Verified directional control and voltage levels
- 	Conducted initial movement tests
Outcomes
- 	L298N driver successfully integrated and verified

**May 19, 2025:** Evaluation of VL53L0X Distance Sensor
Objective
Assess the VL53L0X sensor for short-range distance measurement.
Activities
- 	Mounted sensor and ran calibration routines
- 	Measured response time and accuracy
- 	Compared readings across surface types
Outcomes
- 	Sensor performance evaluated for short-range use

**May 21, 2025:** Servo Motor Installation for Steering Control
Objective
Implement steering mechanism using servo motor.
Activities
- 	Installed servo motor on robotic platform
- 	Conducted range-of-motion tests
- 	Verified responsiveness to control signals
Outcomes
- 	Steering system operational with servo motor

**May 26, 2025:** Initial PWM Test for Speed Control
Objective
Test pulse width modulation for motor speed regulation.
Activities
- 	Configured PWM output from microcontroller
- 	Applied varying duty cycles to motor
- 	Monitored speed response and stability
Outcomes
- 	PWM control validated for speed modulation

**May 27, 2025:** PWM and Servo Synchronization
Objective
Synchronize PWM motor control with servo steering.
Activities
- 	Integrated PWM with L298N driver
- 	Coordinated servo and motor routines
- 	Conducted dynamic movement tests
Outcomes
- 	Synchronized control system operational

**June 2, 2025:** VL53L0X Sensor Integration into Main Program
Objective
Enable continuous distance measurement in core software.
Activities
- 	Embedded sensor polling into main loop
- 	Implemented data filtering and exception handling
- 	Verified real time readings
Outcomes
- 	VL53L0X sensor integrated into robot logic

**June 10, 2025:** Calibration of VL53L0X and Servo Motor
Objective
Fine tune sensor and steering parameters.
Activities
- 	Adjusted sensor thresholds and servo angles
- 	Conducted test runs on base structure
- 	Logged performance metrics
Outcomes
- 	Sensor and servo calibrated for reliable operation

**June 16, 2025:** TCS34725 Sensor Calibration for Color Detection
Objective
Optimize color detection for track recognition.
Activities
- 	Tuned gain and integration time parameters
- 	Tested detection of blue and orange stripes
- 	Logged RGB values for reference
Outcomes
- 	Color sensor calibrated for track conditions

**June 23, 2025:** PID and Distance Measurement Integration
Objective
Combine distance sensing with PID control logic.
Activities
- 	Merged VL53L0X readings with PID routines
- 	Tested response to varying distances
- 	Adjusted PID coefficients
Outcomes
- 	Distance based PID control implemented

**June 30, 2025:** First Program with TCS34725 for Track Detection
Objective
Detect track colors to determine robot course.
Activities
- 	Programmed sensor to identify blue and orange
- 	Mapped color readings to navigation decisions
- 	Conducted initial trials
Outcomes
- 	Track detection logic implemented

**July 1, 2025:** Color Detection Limitations Identified
Objective
Evaluate sensor performance under challenge conditions.
Activities
- 	Tested color detection at competition speed
- 	Logged missed detections and delays
Outcomes
- 	TCS34725 deemed unreliable at high speed

**July 7, 2025:** Replacement of VL53L0X with Ultrasonic Sensor
Objective
Improve distance measurement accuracy.
Activities
- 	Installed ultrasonic sensor
- 	Developed new distance measurement program
- 	Verified sensor response
Outcomes
- 	Ultrasonic sensor adopted for distance sensing

**July 11, 2025:** Hitechnic Sensor Evaluation
Objective
Detect track sections and stopping points.
Activities
- 	Tested detection of blue/orange stripes
- 	Evaluated sensor response at speed
Outcomes
- 	Sensor discarded due to unreliable detection

**July 14–20, 2025:** Structural Component Design and Installation
Objective
Design and install custom mounts for electronics and camera.
Activities
- 	Designed and printed:
- 	Main base (base_principal_v6.stl)
- 	Connector base (base_conector_v3.stl)
- 	Raspberry Pi 5 base (base_pi_5_v5.stl)
- 	Camera base (base_camera_v2.stl)
- 	Camera support (base-Camera-U2.stl)
- 	Camera cover (tapa-Camera.stl)
- 	Mounted components on robot frame
Outcomes
- 	Structural integration of electronics and camera completed
- 	VL53L0X sensor permanently discarded

**July 27–28, 2025:** Camera Configuration and Sensor Integration
Objective
Enable visual processing and sensor communication.
Activities
- 	Configured Pi5 camera for continuous capture
- 	Integrated CV2 for image workflow
- 	Soldered URM37 cables
- 	Verified UART communication
- 	Installed start button
Outcomes
- 	Visual and sensor systems operational

**July 30–31, 2025:** Ultrasonic Sensor Mount and Positioning Program
Objective
Support and utilize ultrasonic sensors for navigation.
Activities
- 	Designed and installed base_urm37_v7.STL
- 	Created program to determine robot position
Outcomes
- 	Position tracking logic implemented

**August 1–2, 2025:** Rotation Sensing and Base Support
Objective
Enable rotation tracking and structural support.
Activities
- 	Read rotation using MPU6050
- 	Applied discrete PID formulas
- 	Designed and printed base_robot_v2.STL
Outcomes
- 	Rotation sensing and support structure completed

**August 4–8, 2025:** Sensor Testing and PID Tuning
Objective
Evaluate alternative sensors and finalize control logic.
Activities
- 	Tested Gy-521 and AS5600 sensors
- 	Discarded AS5600 due to poor performance
- 	Finalized PID tuning
- 	Added BTS7960 driver
- 	Chose ultrasonic sensor for rotation control
Outcomes
- 	PID and sensor configuration finalized

**August 10, 2025:** Challenge 1 Testing and Magnetometer Evaluation
Objective
Complete first challenge and test orientation sensing.
Activities
- 	Ran full challenge simulation
- 	Tested magnetometer for start direction
Outcomes
- 	Magnetometer discarded due to poor accuracy

**August 15–18, 2025:** Image Processing Optimization
Objective
Enable real-time image analysis for block detection.
Activities
- 	Implemented RGB conversion and segmentation
- 	Integrated Cu2 with Pi5
- 	Used NumPy for matrix operations and histogram analysis
- 	Documented use cases in scripts
Outcomes
- 	Image processing routines optimized and validated

**August 23, 2025:** PID Control Adjustments
Objective
Refine navigation control.
Activities
- 	Adjusted PID parameters based on test results
- 	Verified smoother trajectory
Outcomes
- 	Navigation control improved

**August 24–30, 2025:** Challenge Trial Period
Objective
Conduct full challenge simulations.
Activities
- 	Ran repeated trials for both challenges
- 	Logged performance and failure points
Outcomes
- 	Trial data collected for final tuning

**August 30, 2025:** Servo Motor Replacement and Recalibration
Objective
Restore steering functionality.
Activities
- 	Replaced broken servo motor
- 	Recalibrated angles and control parameters
Outcomes
- 	Steering system restored and recalibrated


**September 1–13, 2025:** Technical Documentation Finalization and Software Calibration
Objective
Prepare the system and documentation for the National WRO Competition in Rosarito, Baja California (September 19–20, 2025).
Activities
- Finalized technical documentation, including:
- System architecture overview (hardware/software)
- Wiring diagrams and BOM (Bill of Materials)
- Integrated performance graphs and comparative tables for motor and sensor analysis
- Refined Markdown structure for GitHub repository clarity and sponsor readability
- Calibrated control algorithms for servo response:
- Tuned PID parameters for smoother actuation
- Adjusted PWM ranges
- Conducted functional tests to validate sensor feedback and actuation timing
Outcomes
- Documentation ready for national level technical review
- Software tuned for reliable performance under competition conditions
- GitHub repository updated, sponsor ready materials

[Principal README](https://github.com/CICSA-NET/WRO2025-CICSA/blob/main/README.md)
___

