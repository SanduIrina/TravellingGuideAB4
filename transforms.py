import json
import urllib.request

def elevation(lat, lng):
    apikey = "AIzaSyAkMw5LhNpFJD2X5rnLMYnlLUIl3lM68O8"
    url = "https://maps.googleapis.com/maps/api/elevation/json"
    request = urllib.request.urlopen(url+"?locations="+str(lat)+","+str(lng)+"&key="+apikey)

    results = json.load(request).get('results')
    elevation = results[0].get('elevation')
    # ELEVATION
    print("elevation is")
    print(elevation)
    return elevation
