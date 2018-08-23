import googlemaps
import requests
import responses
import json
import polyline_decoder as pd
import matplotlib.pyplot as plt
import numpy as np
import utm
import map_elements
import math
import numpy as np
from modules.map.proto import map_road_pb2
from utils import distance
from shapely.geometry import LineString, Polygon, Point

from datetime import datetime

#gmaps = googlemaps.Client(key='AIzaSyB7Crz0qA7qyavV-DQHdVyeS2OMvebjtSA')

#now = datetime.now()
#r = gmaps.directions("44.435384, 26.048029",
#                                     "44.436089, 26.045041",
#                                     mode="driving",
#                                     departure_time=now)
#with open('data.json', 'w') as outfile:
#	json.dump(r, outfile)
#print(r)

with open('data.json') as json_data:
    d = json.load(json_data)

decode = d[0]['overview_polyline']['points']
clear = pd.decode_polyline(decode)
print(clear)
x = []
y = []
for i in range(len(clear)):
	xi, yi = utm.from_latlon(clear[i][0],clear[i][1])[0], utm.from_latlon(clear[i][0],clear[i][1])[1]
	x.append(xi)
	y.append(yi)

map = map_pb2.Map()
lane = map.lane.add()
lane.add(clear)

map_file = open('try.txt', 'w')
map_file.write(str(map))
map_file.close()

print(x)
print(y)
