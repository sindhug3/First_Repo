import serial
import time

class serialtest(object):
    def test(self,a):
        ser = serial.Serial ('COM5')    #Open named port
        ser.baudrate = 9600           #Set baud rate to 9600
        #Read ten characters from serial port to data
        ser.write(b'welcome to star2')
        time.sleep(1)
        data1 = ser.read(15)
        return data1
        #Send back the received data
        ser.close()

   

# a=serialtest()

# print(a.test(a))
