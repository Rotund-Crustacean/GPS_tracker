import serial
import io
import time
import os
import NMEA
NMEA = NMEA.NMEA()

#TODO write checksum code
#def calculate_checksum(nmea_sentence):
#   return True


if __name__ == '__main__' :
    try :
        # configure the serial connections (the parameters differs on the device you are connecting to)
        with serial.Serial(port='/dev/cu.usbserial-DK0HDSB8', baudrate=115200) as s:
            for line in s:
                NMEA.decode_line(line)
                print(NMEA.get_lat())
    except ValueError as ve:
        print('Program exit !')
        print(ve)
        pass
    #finally :
        #serial.close()
    pass