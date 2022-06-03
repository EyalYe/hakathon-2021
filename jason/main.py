import requests
import json
import databaseManipulate
import time

# Recieves Locations that are full in json format and returns json format of optimal route
def getOptimalJsonRoute(locations):
    api_key = "03656744-2e3c-4be4-b2f2-767365b28e92"
    response = requests.post("https://graphhopper.com/api/1/vrp?key=" + api_key, json=locations)
    return json.loads(response.text)


# Take Ordered optimal route and make pairs of every 2 destinations
def makeRoutingPairs(jsonRoute):
    coordinates = []
    for destinations in jsonRoute['solution']['routes'][0]['activities']:
        list = []
        list.append(destinations['location_id'])
        list.append(str(destinations['address']['lat']))
        list.append(str(destinations['address']['lon']))
        coordinates.append(list)
    return coordinates


# Creates the exact directions of the route for each endpoint (go left/continue straight etc + coordinates)
def getExplicitRoute(srcLat, srcLon, destLat, destLon):
    api_key = "03656744-2e3c-4be4-b2f2-767365b28e92"
    response = requests.get("https://graphhopper.com/api/1/route?point=" + srcLat + "," + srcLon + "&point=" + destLat + "," + destLon +
                          "&profile=car&locale=en&calc_points=true&points_encoded=false&key=" + api_key)
    return json.loads(response.text)


# Prints textual directions to reach from point to point
def getTextDirections(jsonRoute):
    for directions in jsonRoute['paths'][0]['instructions']:
        print(directions['text'])


# Main program, receives the full trash cans destinations file,
onlyfull_path = r"C:\Users\udial\OneDrive\University\Programming\Python\RouteOptimizer\OnlyFull.json"
numOfIds = 2
while True:
    # Go through all ids, check status and update databese and only full database for routing
    for i in range(numOfIds):
        status = databaseManipulate.get_status(i)
        databaseManipulate.update(i, status)
        databaseManipulate.onlyFullUpdate()

    # open only full trash cans and get the optimal route between them (visit order)
    with open(onlyfull_path, "r+") as file:
        data = json.load(file)
        x = getOptimalJsonRoute(data)

    # make create a between every 2 neighboring trash cans and print the route
    for i in range(len(makeRoutingPairs(x))-1):
        pairs = makeRoutingPairs(x)
        print("routing directions from", pairs[i][0], ":")
        getTextDirections(getExplicitRoute(pairs[i][1], pairs[i][2], pairs[i+1][1],pairs[i+1][2]))

    time.sleep(1800)


#getTextDirections(getExplicitRoute("32.3068650131381", "34.882206380234784", "32.30718239217891", "34.874524533577315"))



