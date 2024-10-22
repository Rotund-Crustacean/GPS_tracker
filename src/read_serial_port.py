import serial;
import io;
import time;
import os;


#TODO write checksum code
#def calculate_checksum(nmea_sentence):
#   return True


if __name__ == '__main__' :
    try :
        # configure the serial connections (the parameters differs on the device you are connecting to)
        with serial.Serial(port='/dev/cu.usbmodem14301', baudrate=115200) as s:
            for line in s:
                str = line.decode('ascii')
                #if 'GLL' in str:
                print(str)
                #interpret_line(line)
    except ValueError as ve:
        print('Program exit !')
        print(ve)
        pass
    finally :
        serial.close()
    pass