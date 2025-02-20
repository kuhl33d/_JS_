import serial
import time

ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1.0)#initialze the serialm communication
time.sleep(3)
ser.reset_input_buffer() #ba5aly el atnen yeklmo ba3d be el function de
print("serial ok")

try:
    
    while True:
         time.sleep(0.1)
         print("sending data to arduino")
         ser.write("hello from raspberry pi".encode('utf-8'))
         time.sleep(1)
         
except KeyboardInterrupt:
    
    print("com stop")
    ser.close()        
