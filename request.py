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
<<<<<<< HEAD
from transforms import elevation
=======
from transforms import *
>>>>>>> 2d23773d7e1a6062ebe23081d6260d7c2eee845f

from datetime import datetime

SOLID_YELLOW = map_lane_pb2.LaneBoundaryType.SOLID_YELLOW
CURB = map_lane_pb2.LaneBoundaryType.CURB
DOTTED_WHITE = map_lane_pb2.LaneBoundaryType.DOTTED_WHITE

# gmaps = googlemaps.Client(key='AIzaSyDpUQ2C21m2UVSZQegN7A9KRrKF2eJHilA')
#|44.435329687380616,26.04523440066663|44.43535548734961,26.045197541858297|44.43574867060316,26.045190510644467|44.435778694988414,26.045152828843335|44.43577881606721,26.045070399472248|44.43579719089836,26.045039189913894|44.4368769407667,26.045001498153535|44.43698902955527,26.0449804472582|44.437285574857746,26.044753584731772|44.43735616812024,26.044722654311354|44.43744624050825,26.04472797204431|44.43748040899487,26.04476599144142|44.4374690694649,26.046662814987037|44.43723878246504,26.047850477805053|44.43722806739574,26.04805546887375|44.43705798665604,26.048993475187572|44.43702516737337,26.049030824227426|44.43696395665587,26.049031817082504|44.436926990463576,26.04904686689156|44.436858904441884,26.049162818854384|44.43668388081901,26.050070487980424|44.43658995074708,26.05026162064497|44.43648113629031,26.0503301050925|44.43638588633527,26.050308402158343|44.43628194900782,26.050205542778443|44.43599848026433,26.049581372298597|44.43597968268387,26.04946456938956|44.435980204537465,26.049073029428218|44.43599633916176,26.048869965425176|44.43597491031456,26.048826460524502|44.435674742627604,26.048673386478367|44.43557385080294,26.048536430359945|44.43544889113353,26.048449874361417|44.43542756786049,26.048440670964766")
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

# with open('data.json') as json_data:
#     d = json.load(json_data)

# decode = d[0]['overview_polyline']['points']
# clear = pd.decode_polyline(decode)
# print(clear)
# x = []
# y = []
points = [[424253.34,4920672.93],
[424016.57,4920669.06],
[424014.36,4920669.06],
[424011.46,4920671.96],
[424011.41,4920715.64],
[424008.45,4920719.01],
[424001.89,4920719.10],
[423999.43,4920721.17],
[423997.83,4920841.14],
[423996.30,4920853.61],
[423978.63,4920886.76],
[423976.26,4920894.63],
[423976.80,4920904.63],
[423979.87,4920908.39],
[424130.81,4920905.37],
[424225.03,4920878.69],
[424241.33,4920877.31],
[424315.76,4920857.55],
[424318.69,4920853.87],
[424318.69,4920847.07],
[424319.84,4920842.95],
[424328.98,4920835.28],
[424400.99,4920815.00],
[424416.08,4920804.39],
[424421.39,4920792.24],
[424419.54,4920781.68],
[424411.22,4920770.23],
[424361.18,4920739.32],
[424351.86,4920737.34],
[424320.70,4920737.76],
[424304.56,4920739.74],
[424301.07,4920737.40],
[424288.50,4920704.20],
[424277.47,4920693.12],
[424270.42,4920679.32],
[424269.66,4920676.96]]

pointsLL = toLatLon(points)
z = []
x = []
y = []
<<<<<<< HEAD
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
=======

# for i in range(len(pointsLL)):
# 	z.append(float(elevation(pointsLL[i][0], pointsLL[i][1])))

# print(z)
# pointsLL = []

# for i in range(len(points)):
# 	pointsLL.append([utm.to_latlon(points[i][0], points[i][1], 35, 'T')])

# print(pointsLL)

#print(utm.from_latlon(clear[1][0],clear[1][1])[2],utm.from_latlon(clear[1][0],clear[1][1])[3])

# xi, yi = utm.from_latlon(clear[0][0],clear[0][1])[0], utm.from_latlon(clear[0][0],clear[0][1])[1]
# xi, yi = points[0][0], points[0][1]
# zi = z[0]
# finalz = []
# if zi != None:
#     zi = float(zi)
# else:
#     print(zi)
#     zi = 200
# for i in range(1,len(points)):
#     x.append(xi)
#     y.append(yi)
#     finalz.append(zi)
#     xn, yn, zn = points[i][0], points[i][1], z[i]
#     xint = (xi + xn)/2
#     yint = (yi + yn)/2
#     zint = (zi + zn)/2
#     x.append(xint)
#     y.append(yint)
#     finalz.append(zint)
#     xi, yi, zi = xn, yn, zn

# points3D = np.array(list(zip(x,y,finalz)))
# # plt.plot(newx, newy)
# # plt.show()
# print(points3D)
# f = open("altitude.txt",'w')
# f.write(points3D)
# f.close()

ppoints = [[4.24253340e+05,4.92067293e+06,8.85452347e+01],
 [4.24134955e+05, 4.92067099e+06, 8.80612221e+01],
 [4.24016570e+05, 4.92066906e+06, 8.75772095e+01],
 [4.24015465e+05, 4.92066906e+06, 8.75834198e+01],
 [4.24014360e+05, 4.92066906e+06, 8.75896301e+01],
 [4.24012910e+05, 4.92067051e+06, 8.75888710e+01],
 [4.24011460e+05, 4.92067196e+06, 8.75881119e+01],
 [4.24011435e+05, 4.92069380e+06, 8.75096703e+01],
 [4.24011410e+05, 4.92071564e+06, 8.74312286e+01],
 [4.24009930e+05, 4.92071732e+06, 8.74095001e+01],
 [4.24008450e+05, 4.92071901e+06, 8.73877716e+01],
 [4.24005170e+05, 4.92071905e+06, 8.73833351e+01],
 [4.24001890e+05, 4.92071910e+06, 8.73788986e+01],
 [4.24000660e+05, 4.92072013e+06, 8.73798485e+01],
 [4.23999430e+05, 4.92072117e+06, 8.73807983e+01],
 [4.23998630e+05, 4.92078115e+06, 8.66264725e+01],
 [4.23997830e+05, 4.92084114e+06, 8.58721466e+01],
 [4.23997065e+05, 4.92084738e+06, 8.56517334e+01],
 [4.23996300e+05, 4.92085361e+06, 8.54313202e+01],
 [4.23987465e+05, 4.92087019e+06, 8.48463249e+01],
 [4.23978630e+05, 4.92088676e+06, 8.42613297e+01],
 [4.23977445e+05, 4.92089070e+06, 8.41008606e+01],
 [4.23976260e+05, 4.92089463e+06, 8.39403915e+01],
 [4.23976530e+05, 4.92089963e+06, 8.37242355e+01],
 [4.23976800e+05, 4.92090463e+06, 8.35080795e+01],
 [4.23978335e+05, 4.92090651e+06, 8.34664268e+01],
 [4.23979870e+05, 4.92090839e+06, 8.34247742e+01],
 [4.24055340e+05, 4.92090688e+06, 8.07632256e+01],
 [4.24130810e+05, 4.92090537e+06, 7.81016769e+01],
 [4.24177920e+05, 4.92089203e+06, 7.82969017e+01],
 [4.24225030e+05, 4.92087869e+06, 7.84921265e+01],
 [4.24233180e+05, 4.92087800e+06, 7.84505196e+01],
 [4.24241330e+05, 4.92087731e+06, 7.84089127e+01],
 [4.24278545e+05, 4.92086743e+06, 7.82552795e+01],
 [4.24315760e+05, 4.92085755e+06, 7.81016464e+01],
 [4.24317225e+05, 4.92085571e+06, 7.81825752e+01],
 [4.24318690e+05, 4.92085387e+06, 7.82635040e+01],
 [4.24318690e+05, 4.92085047e+06, 7.83428955e+01],
 [4.24318690e+05, 4.92084707e+06, 7.84222870e+01],
 [4.24319265e+05, 4.92084501e+06, 7.84360619e+01],
 [4.24319840e+05, 4.92084295e+06, 7.84498367e+01],
 [4.24324410e+05, 4.92083912e+06, 7.84557266e+01],
 [4.24328980e+05, 4.92083528e+06, 7.84616165e+01],
 [4.24364985e+05, 4.92082514e+06, 7.87393456e+01],
 [4.24400990e+05, 4.92081500e+06, 7.90170746e+01],
 [4.24408535e+05, 4.92080970e+06, 7.94723969e+01],
 [4.24416080e+05, 4.92080439e+06, 7.99277191e+01],
 [4.24418735e+05, 4.92079831e+06, 8.04036407e+01],
 [4.24421390e+05, 4.92079224e+06, 8.08795624e+01],
 [4.24420465e+05, 4.92078696e+06, 8.13284569e+01],
 [4.24419540e+05, 4.92078168e+06, 8.17773514e+01],
 [4.24415380e+05, 4.92077596e+06, 8.23671608e+01],
 [4.24411220e+05, 4.92077023e+06, 8.29569702e+01],
 [4.24386200e+05, 4.92075478e+06, 8.46299019e+01],
 [4.24361180e+05, 4.92073932e+06, 8.63028336e+01],
 [4.24356520e+05, 4.92073833e+06, 8.64460373e+01],
 [4.24351860e+05, 4.92073734e+06, 8.65892410e+01],
 [4.24336280e+05, 4.92073755e+06, 8.67496338e+01],
 [4.24320700e+05, 4.92073776e+06, 8.69100266e+01],
 [4.24312630e+05, 4.92073875e+06, 8.69387627e+01],
 [4.24304560e+05, 4.92073974e+06, 8.69674988e+01],
 [4.24302815e+05, 4.92073857e+06, 8.70297127e+01],
 [4.24301070e+05, 4.92073740e+06, 8.70919266e+01],
 [4.24294785e+05, 4.92072080e+06, 8.77031746e+01],
 [4.24288500e+05, 4.92070420e+06, 8.83144226e+01],
 [4.24282985e+05, 4.92069866e+06, 8.83643875e+01],
 [4.24277470e+05, 4.92069312e+06, 8.84143524e+01],
 [4.24273945e+05, 4.92068622e+06, 8.84729385e+01],
 [4.24270420e+05, 4.92067932e+06, 8.85315247e+01],
 [4.24270040e+05, 4.92067814e+06, 8.85320969e+01]]

zen = []
finestz = []
a = []
b = []
for i in range(len(ppoints)):
	zen.append(ppoints[i][2])
	if(i%2 == 0):
		#finestz.append(ppoints[i][2])
		finestz.append(0)
		a.append(ppoints[i][0])
		b.append(ppoints[i][1])
a.append(a[0])
b.append(b[0])
finestz.append(finestz[0])
finestp = np.array(list(zip(a,b,finestz)))
>>>>>>> 2d23773d7e1a6062ebe23081d6260d7c2eee845f

map = map_pb2.Map()
laneL = Lane(1, map)
laneR = Lane(2, map)
left_lane_x, right_lane_x, left_lane_y, right_lane_y = laneL.justGetMeTheLanes(finestp, 3)

left_points = []
left_points = np.array(list(zip(left_lane_x, left_lane_y, finestz)))
laneL.add(left_points, 30, map_lane_pb2.Lane.NO_TURN, map_lane_pb2.Lane.CITY_DRIVING, map_lane_pb2.Lane.FORWARD, 3)
laneL.add_overlap(1)
laneL.set_left_lane_boundary_type(CURB, True)
laneL.set_right_lane_boundary_type(DOTTED_WHITE, False)

right_points = []
right_points = np.array(list(zip(right_lane_x, right_lane_y, finestz)))
laneR.add(right_points, 30, map_lane_pb2.Lane.NO_TURN, map_lane_pb2.Lane.CITY_DRIVING, map_lane_pb2.Lane.FORWARD, 3)
laneR.add_overlap(2)
laneR.set_left_lane_boundary_type(DOTTED_WHITE, False)
laneR.set_right_lane_boundary_type(CURB, True)

map_file = open('try.txt', 'w')
map_file.write(str(map))
map_file.close()

