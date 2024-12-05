import time
import threading
import Adafruit_BBIO.GPIO as GPIO
from opc import Client

# Configuration
BUTTON_PIN = "P2_2"  # Corrected GPIO pin for button
OPC_SERVER_ADDRESS = "localhost:7890"
LED_COUNT = 60  # Total number of LEDs (2 strips of 30)

# Global state variables
led_on = False
current_color = (255, 0, 0)  # Default color (red)
BUTTON_HOLD_TIME = 1.0  # Time in seconds to distinguish a hold from a press

# Predefined colors for cycling
COLOR_LIST = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (255, 255, 255),  # White
]

# OPC client setup
opc_client = Client(OPC_SERVER_ADDRESS)
if not opc_client.can_connect():
    print("Warning: Could not connect to OPC server.")
else:
    print("Connected to OPC server.")

# Functions for LED control
def toggle_lights(state):
    """Turn lights on or off based on state."""
    global led_on
    if state:
        opc_client.put_pixels([current_color] * LED_COUNT)
        led_on = True
        print(f"Lights turned ON with color: {current_color}")
    else:
        opc_client.put_pixels([(0, 0, 0)] * LED_COUNT)
        led_on = False
        print("Lights turned OFF")

def get_next_color(current_color):
    """Cycle to the next color in the predefined list."""
    index = COLOR_LIST.index(current_color)
    return COLOR_LIST[(index + 1) % len(COLOR_LIST)]

# Button callbacks
def button_press_callback():
    """Handle single button press to change colors or turn lights on."""
    global current_color
    if led_on:
        current_color = get_next_color(current_color)
        opc_client.put_pixels([current_color] * LED_COUNT)
        print(f"Color changed to: {current_color}")
    else:
        toggle_lights(True)

def button_hold_callback():
    """Handle button hold to turn lights off."""
    if led_on:
        toggle_lights(False)

def button_handler(channel):
    """Distinguish between press and hold."""
    start_time = time.time()
    while GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Wait while button is held
        time.sleep(0.01)  # Debounce delay
    duration = time.time() - start_time

    if duration >= BUTTON_HOLD_TIME:
        button_hold_callback()
    else:
        button_press_callback()

# GPIO setup for button
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_handler, bouncetime=200)

# Main loop
print("Ready! Use the button to control the LEDs.")
try:
    while True:
        time.sleep(1)  # Keep the script running
except KeyboardInterrupt:
    print("Exiting program...")
    GPIO.cleanup()
    toggle_lights(False)  # Ensure LEDs are turned off on exit
