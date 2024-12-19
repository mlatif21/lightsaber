# Lightsaber
## ENGI301 lightsaber project (in progress)

The files in this repository contain the code required to fun the different functions of the lightsaber.
Link to the Hackster page describing the project: https://www.hackster.io/mustafa-latif/edes301-lightsaber-2d389d

My portion of the project focused on functionality of the button control and the LED light strips. The file lightsaber_lights.py encodes for the lights to turn on upon a button press, change colors upon further consecutive button presses, and turn off when the button is held.

Liam McConnico-Blanchet's division of the project was related to the IMU and speakers. Eventually, the code for each component will be implemented into a single script to run all lightsaber functions simultaneously.

### **Lights**

The following files from Erik Welsh were used for OPC configuration for the LED light strip software set up. The PRU files must be in the pru/bin/ subdirectory from the opc-server executable function.
- configure_pins.sh
- run
- run-opc-server
- opc-server
- opc.py
- config.json
- pru/bin/ws281x-original-ledscape-pru0.bin
- pru/bin/ws281x-original-ledscape-pru1.bin

The primary file for the lightsaber functionality is lightsaber_lights.py. To run this code, the following must be run in the terminal:
sudo ./run-opc-server

In a separate terminal, the main script can be run using:
python3 lightsaber_lights.py

The remaining files in this directory were minimal tests for the LED strip to debug the light's software.

### **Button**

The button_tester.py file was used to test proper hardware integration of the button and is used from Erik Welsh. The variables and states used within this file are applied within the lightsaber_lights.py file that allows for the light and button combined functionality.

### **IMU**

The code for the IMU was downloaded from Liam McConnico-Blanchet's repository. The mpu6050.py script measures data from the IMU and can detect impact of the device.

## Future Steps

I2S functionality on the PocketBeagle is causing us problems in configuration, so we do not have functional speakers yet. The next step is to integrate the hit-detection from the IMU script with the lights so that the lights respond on impact and movement. Once the speakers are functional, we can then introduce hit and swinging sounds to the IMU and light functionality, completing the integration for the project.
