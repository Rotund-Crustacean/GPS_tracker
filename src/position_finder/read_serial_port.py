import serial
from src.position_finder import manage_influxdb, NMEA

NMEA = NMEA.NMEA()

#TODO write checksum code
#def calculate_checksum(nmea_sentence):
#   return True


if __name__ == '__main__' :
    #defining classes
    current_influxdb = manage_influxdb.manage_influxdb("HsevzKSY5KVO3fMpTD-vVIgre-lQKsmGyYMxorhF-yPcxI5qjmdIGOqPOrTNvkGG_jYbPf3AX3vSipY-apjsBw==", "gps_tracker", "http://localhost:8086", "coordinates", "vehicle1")
    current_position_data = None
    # try :
    # configure the serial connections (the parameters differs on the device you are connecting to)
    with serial.Serial(port='/dev/cu.usbmodem14301', baudrate=115200) as s:
        for line in s:
            NMEA.decode_line(line)
            new_position_data = NMEA.get_position_data()
            #updating current_position_data from None on first pass
            if current_position_data == None:
                current_position_data = new_position_data
            if new_position_data != None:
                #comparing if new read location is the same as most recent read location
                if not new_position_data.equals(current_position_data):
                    current_influxdb.write(new_position_data)
                    current_position_data = new_position_data
    # except ValueError as ve:
    #     print('Program exit ! ' , ve)
    #     print(ve.)

    #finally :
        #serial.close()


#influxdb