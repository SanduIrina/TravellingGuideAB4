import googlemaps
import requests
import responses
import json
import polyline_decoder as pd
import matplotlib.pyplot as plt
import numpy as np
import utm
from map_elements import *
import math
import numpy as np
from modules.map.proto import map_road_pb2
from modules.map.proto import map_pb2
from modules.map.proto import map_lane_pb2
from utils import distance
from shapely.geometry import LineString, Polygon, Point
from transforms import elevation

from datetime import datetime

SOLID_YELLOW = map_lane_pb2.LaneBoundaryType.SOLID_YELLOW
CURB = map_lane_pb2.LaneBoundaryType.CURB
DOTTED_WHITE = map_lane_pb2.LaneBoundaryType.DOTTED_WHITE

# gmaps = googlemaps.Client(key='AIzaSyDpUQ2C21m2UVSZQegN7A9KRrKF2eJHilA')

# now = datetime.now()
# r = gmaps.directions("44.435385, 26.048263",
#                                     "44.435435, 26.048435",
#                                     waypoints=["44.435328, 26.045326",
#                                     			"44.435378, 26.045200",
#                                     			"44.435721, 26.045187",
# 												"44.435902, 26.045027",
# 												"44.436880, 26.044993",
# 												"44.437291, 26.044750",
# 												"44.437462, 26.046581",
# 												"44.437103, 26.048826",
# 												"44.436864, 26.049158",
# 												"44.435989, 26.049539"],
#                                     mode="driving",
#                                     departure_time=now)
# with open('data.json', 'w') as outfile:
# 	json.dump(r, outfile)
# print(r)

with open('data.json') as json_data:
    d = json.load(json_data)

decode = d[0]['overview_polyline']['points']
clear = pd.decode_polyline(decode)
print(clear)
x = []
y = []
z = []
points = []
# for i in range(len(clear)):
# 	xi, yi = utm.from_latlon(clear[i][0],clear[i][1])[0], utm.from_latlon(clear[i][0],clear[i][1])[1]
# 	if(i > 0):
# 		intx = (xi + nxi)/2
# 		inty = (yi + nyi)/2
# 		intz = elevation(intx, inty)
# 		x.append(intx)
# 		y.append(inty)
# 		z.append(intz)
# 	nxi, nyi = xi, yi
# 	intz = elevation(xi, yi)
# 	x.append(xi)
# 	y.append(yi)
# 	z.append(intz)

xi, yi = utm.from_latlon(clear[0][0],clear[0][1])[0], utm.from_latlon(clear[0][0],clear[0][1])[1]
zi = elevation(clear[0][0],clear[0][1])
if zi != None:
	zi = float(zi)
else:
	print(zi)
	zi = 200
for i in range(1,len(clear)):
	x.append(xi)
	y.append(yi)
	z.append(zi)
	xn, yn = utm.from_latlon(clear[i][0],clear[i][1])[0], utm.from_latlon(clear[i][0],clear[i][1])[1]
	zn = elevation(clear[i][0],clear[i][1])
	if zn != None:
		zn = float(zn)
	else:
		print(zi)
		zn = 200
	xint = (xi + xn)/2
	yint = (yi + yn)/2
	zint = (zi + zn)/2
	x.append(xint)
	y.append(yint)
	z.append(zint)
	xi, yi, zi = xn, yn, zn

# newx = []
# newy = []
# for i in range(len(x)):
# 	xi, yi = x[i], y[i]
# 	if(i > 0):
# 		intx = (xi + nxi)/2
# 		inty = (yi + nyi)/2
# 		newx.append(intx)
# 		newy.append(inty)
# 	nxi, nyi = xi, yi
# 	newx.append(xi)
# 	newy.append(yi)

# nnewx = []
# nnewy = []
# for i in range(len(newx)):
# 	xi, yi = newx[i], newy[i]
# 	if(i > 0):
# 		intx = (xi + nxi)/2
# 		inty = (yi + nyi)/2
# 		nnewx.append(intx)
# 		nnewy.append(inty)
# 	nxi, nyi = xi, yi
# 	nnewx.append(xi)
# 	nnewy.append(yi)

points = np.array(list(zip(x,y,z)))
# plt.plot(newx, newy)
# plt.show()
print(points)

map = map_pb2.Map()
laneL = Lane(1, map)
laneR = Lane(2, map)
left_lane_x, right_lane_x, left_lane_y, right_lane_y = laneL.justGetMeTheLanes(points, 3.3)

left_points = []
left_points = np.array(list(zip(left_lane_x, left_lane_y)))
laneL.add(left_points, 30, map_lane_pb2.Lane.NO_TURN, map_lane_pb2.Lane.CITY_DRIVING, map_lane_pb2.Lane.FORWARD, 3.3)
laneL.add_overlap(1)
laneL.set_left_lane_boundary_type(CURB, True)
laneL.set_right_lane_boundary_type(DOTTED_WHITE, True)

right_points = []
right_points = np.array(list(zip(right_lane_x, right_lane_y)))
laneR.add(right_points, 30, map_lane_pb2.Lane.NO_TURN, map_lane_pb2.Lane.CITY_DRIVING, map_lane_pb2.Lane.FORWARD, 3.3)
laneR.add_overlap(2)
laneR.set_left_lane_boundary_type(DOTTED_WHITE, True)
laneR.set_right_lane_boundary_type(CURB, True)

map_file = open('try.txt', 'w')
map_file.write(str(map))
map_file.close()
