import requests
import json
import matplotlib.pyplot as plt

URL = "https://route.api.here.com/routing/7.2/calculateroute.json"
app_id = "4vLKaRQKmQntLxTx1xTQ"
app_code = "o4QIs2e7W_3BiHi2XeB2jQ"
waypoint0 = "44.435391,26.048103"
waypoint1 = "44.435335,26.045179"
waypoint2 = "44.435756,26.045158"
waypoint3 = "44.435777,26.04506"
waypoint4 = "44.43703,26.04459"
mode = "fastest;car;traffic:disabled"
PARAMS = {'app_id':app_id,
			'app_code':app_code,
			'waypoint0':waypoint0,
			'waypoint1':waypoint1,
			'waypoint2':waypoint2,
			'waypoint3':waypoint3,
			'waypoint1':waypoint4,
			'mode':mode,
			'routeattributes':"shape"}
r = requests.get(url = URL, params = PARAMS)
print(r.status_code)
data = r.json()
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
shape = data["response"]["route"][0]["shape"]
new_data = []
for i in range(len(shape)):
	s = ''.join(shape[i])
	s = s.split(",")
	s[0], s[1] = float(s[0]), float(s[1])
	new_data.append(s)
print(new_data)
plt.plot(new_data)
plt.show()
