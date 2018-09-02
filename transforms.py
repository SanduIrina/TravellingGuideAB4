<<<<<<< HEAD
=======
import utm
import numpy as np
>>>>>>> 2d23773d7e1a6062ebe23081d6260d7c2eee845f
import json
import urllib.request

def elevation(lat, lng):
<<<<<<< HEAD
    apikey = "AIzaSyAkMw5LhNpFJD2X5rnLMYnlLUIl3lM68O8"
    url = "https://maps.googleapis.com/maps/api/elevation/json"
    request = urllib.request.urlopen(url+"?locations="+str(lat)+","+str(lng)+"&key="+apikey)

    results = json.load(request).get('results')
    elevation = results[0].get('elevation')
    # ELEVATION
    print("elevation is")
    print(elevation)
    return elevation
=======
    apikey = "AIzaSyDAeuq1vXAszCNF9HhLIadyToJ44OSJMMQ"
    url = "https://maps.googleapis.com/maps/api/elevation/json"
    request = urllib.request.urlopen(url+"?locations="+str(lat)+","+str(lng)+"&key="+apikey)
    results = json.load(request).get('results')
    elevation = results[0].get('elevation')
    return elevation

def toLatLon(points):
    pointsLL = []
    for i in range(len(points)):
        pointsLL.append(utm.to_latlon(points[i][0], points[i][1], 35, 'T'))
    pointsLL = np.array(pointsLL)
    return pointsLL
>>>>>>> 2d23773d7e1a6062ebe23081d6260d7c2eee845f
