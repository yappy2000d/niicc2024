import threading
import serial
from serial import SerialException

ser = serial.Serial('COM6', 9600, timeout=1)
# ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) # Linux 上使用 /dev/ttyUSB0

def send(lettuce_val, potato_val, carrot_val, onion_val, garlic_val, leek_val, broccoli_val):
    if not ser.is_open:
        raise SerialException("Serial port is not open")
    
    payload = f"lettuce:{lettuce_val},potato:{potato_val},carrot:{carrot_val},onion:{onion_val},garlic:{garlic_val},leek:{leek_val},broccoli:{broccoli_val}\n"
    ser.write(payload.encode('utf-8'))
    
def receive():
    while True:
        if ser.is_open:
            data = ser.readline().decode('utf-8').strip()
            if data:
                print(f"Received from Arduino: {data}")
                
            data_map = {
                '1': 'Recipe1',
                '2': 'Recipe2',
                '3': 'Recipe3'
            }
            
            print(data_map.get(data, 'Unknown') + "OK!")
