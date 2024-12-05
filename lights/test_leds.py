from opc import Client

# Configuration
OPC_SERVER_ADDRESS = "localhost:7890"
LED_COUNT = 60  # Total LEDs (2 strips of 30)

# Connect to OPC server
opc_client = Client(OPC_SERVER_ADDRESS)
if not opc_client.can_connect():
    print("Warning: Could not connect to OPC server.")
else:
    print("Connected to OPC server.")

def send_led_data(color):
    """Send a single color to all LEDs."""
    leds = [color] * LED_COUNT  # Create an array with the same color for all LEDs
    opc_client.put_pixels(leds)
    opc_client.put_pixels(leds)  # Send twice for reliability
    print(f"LEDs set to color: {color}")

# Test the LEDs with a solid color
try:
    send_led_data((255, 0, 0))  # Red color for testing
    input("Press Enter to clear LEDs...")
    send_led_data((0, 0, 0))  # Turn off all LEDs
except KeyboardInterrupt:
    send_led_data((0, 0, 0))  # Ensure LEDs are off on exit
