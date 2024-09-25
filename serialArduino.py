import serial
import time

class SerialArduino():
    def sendBytes(self, data):
      arduino = serial.Serial('/dev/ttyUSB0', 9600)
      #print(arduino.name)
      #time.sleep(0.1) # Espera a que la conexion se establezca
      arduino.write(bytes(data)) #Solo puedo enviar hasta 256 valores
      #time.sleep(0.1)
      arduino.close()

if __name__ == "__main__":
    arduino = SerialArduino()
    data=[144,100,255,1,2,3]
    arduino.sendBytes(data)

#todo Enviar una lista con los resultados observados por handTracking, probar cada cuantos valores deberia enviar el array