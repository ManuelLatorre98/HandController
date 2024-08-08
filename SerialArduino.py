import serial
import time

arduino = serial.Serial('/dev/ttyUSB0', 9600)
print(arduino.name)

time.sleep(2) # Espera a que la conexion se establezca
arduino.write(b'AAA')
# data = [0, 1, 1, 0, 1]
#
# for value in data:
#     arduino.write(bytes([value]))
#     time.sleep(1)

arduino.close()
