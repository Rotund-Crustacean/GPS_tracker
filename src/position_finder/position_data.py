#location data class
class position_data:

    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon
        return


    #getters and setters
    def get_lat(self):
        return self.lat

    def get_lon(self):
        return self.lon

    # comparing if two position_data objects are identical
    def equals(self, position_data):
        if self.lat != position_data.get_lat():
            return False
        if self.lon != position_data.get_lon():
            return False

        return True

    def get_position_as_xy(self):
        #returning lat and lon as coordinates
        return(self.lat, self.lon)