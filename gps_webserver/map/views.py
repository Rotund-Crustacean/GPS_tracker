from django.shortcuts import render
from django.http import JsonResponse
from influxdb_client import InfluxDBClient
import json
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Pins

@login_required
def index(request):
    context = dict()
    return render(request, "map/index.html", context)

@login_required
def main_screen(request):
    username = None
    context = dict()

    #This code is all functional, but cannot be used by the template
    #so has been commented out

    #all_pins = []
    #for all rows in the pins table
    #current_row = Pins.objects.count()
    #while current_row > 0:
        #temp_pins_dict = {}
        #finds each line where primary key = current_row, then inputs each
        #column of data as a seperate entry into a dictionary
        #This is at best very unoptimised
        #row = Pins.objects.get(pk=current_row)
        #temp_pins_dict['lat'] = row.lat
        #temp_pins_dict['lon'] = row.lon
        #temp_pins_dict['content'] = row.content
        #appends that dictionary to a list of dictionaries
        #all_pins.append(temp_pins_dict)
        #current_row = current_row - 1

    #adds the list of dictionaries to the context to be sent to the template
    #context['pins_data'] = all_pins

    #fetching username for context
    if request.user.is_authenticated:
        username = request.user.username
        print(username)
        context['username'] = username

    return render(request, "map/main-screen.html", context)


@csrf_exempt
@login_required
def positions(request):
    #definning variables
    position_data = []

    #filtering out non-POST requests
    if request.method == "POST":

        #decodes binary request into regular string
        #loads string into a python dictionary
        #defines dictionary a request_body variable
        request_body = json.loads(request.body.decode('utf-8'))

        #defining query variables from request input
        #needs to be changed with improvements to allow different buckets for different
        #users on one production website
        bucket = 'coordinates'

        #retrieving useful data from the request
        #time is an integer in days
        time_start = request_body['start']
        time_end = request_body['end']
        vehicle = request_body['vehicle']

        #retrieving influx data
        result = __get_influx_data(bucket, time_start, time_end, vehicle)

        for row in result:
            this_pd = {}
            #filtering empty rows
            if row != '\n':
                #filtering annotation rows
                if row[6] == 'coordinates':
                    #extracting and storing data
                    this_pd['time'] = row[5]
                    this_pd['vehicle'] = row[7]

                    lon = float(row[8])
                    this_pd['lon'] = lon

                    lat = float(row[9])
                    this_pd['lat'] = lat

                    position_data.append(this_pd)

        #returning list of dictionaries as a JSON response

        return JsonResponse({"position_data": position_data})
    else:
        #this does pretty much nothing, but it won't crash when receiving invalid data
        return(HttpResponse('Invalid Request'))

def __get_influx_data(bucket, time_start, time_stop, vehicle):
    #initialising influx client
    client = InfluxDBClient(url="http://localhost:8086",
                            token="HsevzKSY5KVO3fMpTD-vVIgre-lQKsmGyYMxorhF-yPcxI5qjmdIGOqPOrTNvkGG_jYbPf3AX3vSipY-apjsBw==",
                            org="gps_tracker")
    #setting to query api
    query_api = client.query_api()

    #f'|>filter(fn: (r) => r.vehicle_id == "{vehicle}")'

    #making query
    result = query_api.query_csv(f'from(bucket:"{bucket}") '
        f'|>range(start:-{time_start}d, stop:-{time_stop}d) '
        f'|>filter(fn: (r) => r._measurement == "coordinates")'
        f'|>filter(fn: (r) => r.vehicle_id == "{vehicle}")'
        f'|>filter(fn: (r) => r._field == "lat" or r._field == "lon")'
        f'|> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")')

    #print(result)

    return result
