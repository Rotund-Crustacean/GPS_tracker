from position_data import position_data as pd
class NMEA:

    #initialising
    def __init__(self):
        self.pd = None
        return

    #getter
    def get_position_data(self):
        return self.pd

    #method for decoding NMEA messages
    def decode_line(self, line):
        #converting from binary string to ascii string
        _line = line.decode('ascii')
        if _line[3:6] == 'GLL':
            NMEA.__decode_GLL(self,_line)

    #method for decoding specifically GLL messages
    #updates position_data class when run
    def __decode_GLL(self,line):
        #splits message into an array
        line_parts = line.split(',')

        #determines whether lat and lon should be positive or negative
        if line_parts[1] != '' or  line_parts[3] != '':
            if line_parts[2] == 'S':
                lat = NMEA.__convert_to_decimal_degrees(line_parts[1]) * -1
            elif line_parts[2] == 'N':
                lat = NMEA.__convert_to_decimal_degrees(line_parts[1])
            # really should bring up an error if it is neither
            if line_parts[4] == 'W':
                lon = NMEA.__convert_to_decimal_degrees(line_parts[3]) * -1
            elif line_parts[4] == 'E':
                lon = NMEA.__convert_to_decimal_degrees(line_parts[3])
            # really should bring up an error if it is neither

            #updates self.pd object with lat and lon
            self.pd = pd(lat,lon)


    #converts degrees and minutes coordinates to minutes coordinates
    @staticmethod
    def __convert_to_decimal_degrees(ddmm):
        ddmm = str(ddmm)
        ddmm_split = ddmm.split('.')
        int_ddmm = ddmm_split[0]
        #dealing with the variable number of degrees at the start of the message
        int_degrees = int(int_ddmm[0:len(int_ddmm)-2])
        int_minutes = int(int_ddmm[len(int_ddmm)-2:len(int_ddmm)])
        float_minutes = float('0.' + ddmm_split[1])
        decimal_degrees = int_degrees + (int_minutes + float_minutes) / 60
        return decimal_degrees


