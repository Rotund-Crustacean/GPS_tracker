import influxdb_client, os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# token = "HsevzKSY5KVO3fMpTD-vVIgre-lQKsmGyYMxorhF-yPcxI5qjmdIGOqPOrTNvkGG_jYbPf3AX3vSipY-apjsBw=="
# org = "gps_tracker"
# url = "http://localhost:8086"
# bucket = "coordinates"
# measurement = "coordinates"

class manage_influxdb:

    def __init__(self, token, org, url, bucket, tag):
        # token is the API access token
        # org is the organisation to access
        self.org = org  # URL of influxdb
        self._bucket = bucket # name of bucket to access
        self._tag = tag # data tag / index e.g tracker id
        write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=self.org)
        self.write_api = write_client.write_api(write_options=SYNCHRONOUS) # creating write_api object as attribute

    # defining getters and setters
    # likely unnecessary
    # <editor-fold desc="getters and setters">
    def get_token(self):
        return self.token

    def set_token(self,token):
        self.token = token

    def get_org(self):
        return self.org

    def set_org(self,org):
        self.org = org

    def get_url(self):
        return self.url

    def set_url(self,url):
        self.url = url

    def get_bucket(self):
        return self.bucket

    def set_bucket(self,bucket):
        self.bucket = bucket

    def get_tag(self):
        return self.tag

    def set_tag(self,tag):
        self.tag = tag
    # </editor-fold>

    #write takes in a position_data class and puts it in the database
    def write(self, new_position_data):
        point = (
            Point("coordinates")
            .tag("vehicle_id", self._tag)
            .field("lat", new_position_data.get_lat())
            .field("lon", new_position_data.get_lon())
            )

        self.write_api.write(bucket = self._bucket, org = self.org, record=point)
