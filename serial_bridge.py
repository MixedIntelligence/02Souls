# serial_bridge.py Add emotion_bridge.py call and send behavior command to Arduino.

import serial
import time
from emotion_bridge import get_primary_action

# Adjust this to your system's serial port
SERIAL_PORT = '/dev/ttyACM0'
BAUD_RATE = 9600

def send_to_robot(command):
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
        ser.write(f"{command}\n".encode('utf-8'))
        print(f"Sent: {command}")
        time.sleep(1)

if __name__ == "__main__":
    mood = input("📝 Describe how you're feeling:\n> ")
    action = get_primary_action(mood)
    send_to_robot(action)
