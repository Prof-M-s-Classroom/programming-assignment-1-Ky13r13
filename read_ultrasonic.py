import serial
import time
from distance import Distance
from stack import CircularStack
# Change 'COM3' to your actual Arduino port (Linux:'/dev/ttyUSB0', Mac: '/dev/tty.usbmodem*')
arduino = serial.Serial('COM5', 9600)
time.sleep(2) # Allow connection to establish
stack = CircularStack()
try:
    while True:
        if arduino.in_waiting > 0: # Check if data is available
            raw_distance = arduino.readline().decode('utf-8').strip()

            try:
                # Convert distance to a float and create a Distance object
                distance_value = float(raw_distance)
                distance_obj = Distance(distance_value)

                # Push to stack
                stack.push(distance_obj)

                # Print the stack to verify 
                print("\nCurrent Stack Contents:")
                stack.print_stack()

            except ValueError:
                print(f"Invalid data received: {raw_distance}")

        time.sleep(2)
except KeyboardInterrupt:
    print("Exiting...")
    arduino.close()
