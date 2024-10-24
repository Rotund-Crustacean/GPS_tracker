import logging

class NMEA:

    #initialising attributes
    def __init__(self):
        self.lat = 0.0
        self.lat_sign = ''
        self.lon = 0.0
        self.lon_sign = ''
        return

    #getters for class attributes
    def get_lat(self):
        return self.lat

    def get_lat_sign(self):
        return self.lat_sign

    def get_lon(self):
        return self.lon

    def get_lon_sign(self):
        return self.lon_sign

    #method for decoding NMEA messages
    def decode_line(self,line):
        #converting from binary string to ascii string
        _line = line.decode('ascii')
        if _line[3:6] == 'GLL':
            NMEA.__decode_GLL(self,_line)

    #method for decoding specifically GLL messages
    #updates attributes when called, acts as a setter
    def __decode_GLL(self,line):
        print("Decoding " + line)
        line_parts = line.split(',')
        self.lat = line_parts[1]
        self.lat_sign = line_parts[2]
        self.lon = line_parts[3]
        self.lon_sign = line_parts[4]


