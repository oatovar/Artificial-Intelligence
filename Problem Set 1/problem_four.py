#!/usr/bin/env python3

# Using the great-circle distance for higher accuracy.
from geopy.distance import geodesic

class City:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.vertices = dict()

    def __str__(self):
        return self.name

    def add(self, vertice, distance):
        self.vertices[vertice] = distance
    
    def remove(self, vertice):
        self.vertices.pop(vertice)

    def getDistance(self, city):
        return self.vertices[city]
    
    def getCoordinates(self):
        return self.coordinates

def printChoices(graph):
    for index, city in enumerate(graph):
        print(index, ":", city)

# Cities that are allowed within program.
new_york = City("New York", (40.730610, -73.935242))
los_angeles = City("Los Angeles", (34.052235, -118.243683))
chicago = City("Chicago", (41.881832, -87.623177))
minneapolis = City("Minneapolis", (44.986656, -93.258133))
denver = City("Denver", (39.742043, -104.991531))
dallas = City("Dallas", (32.897480, -97.040443))
seattle = City("Seattle", (47.608013, -122.335167))
boston = City("Boston", (42.361145, -71.057083))
san_francisco = City("San Francisco", (37.7749, -122.4194))
st_louis = City("St. Louis", (38.627003, -90.199402))
houston = City("Houston", (29.7604, -95.3698))
phoenix = City("Phoenix", (33.448376, -112.074036))
salt_lake_city = City("Salt Lake City", (40.7608, -111.8910))

# Create graph with the cities.
graph = list()
graph.append(new_york)
graph.append(los_angeles)
graph.append(chicago)
graph.append(minneapolis)
graph.append(denver)
graph.append(dallas)
graph.append(seattle)
graph.append(boston)
graph.append(san_francisco)
graph.append(st_louis)
graph.append(houston)
graph.append(phoenix)
graph.append(salt_lake_city)

# Append destinations and length for each city
# New York valid destinations
new_york.add(new_york, 0)
# new_york.add(los_angeles, 10000)
new_york.add(chicago, 713)
new_york.add(minneapolis, 1018)
# new_york.add(denver, 10000)
new_york.add(dallas, 1374)
# new_york.add(seattle, 10000)
new_york.add(boston, 213)
# new_york.add(san_francisco, 10000)
new_york.add(st_louis, 875)
# new_york.add(houston, 10000)
# new_york.add(phoenix, 10000)
# new_york.add(salt_lake_city, 10000)

# Los Angeles valid destinations
# los_angeles.add(new_york, 10000)
los_angeles.add(los_angeles, 0)
# los_angeles.add(chicago, 10000)
# los_angeles.add(minneapolis, 10000)
los_angeles.add(denver, 831)
los_angeles.add(dallas, 1240)
los_angeles.add(seattle, 959)
# los_angeles.add(boston, 10000)
los_angeles.add(san_francisco, 403)
# los_angeles.add(st_louis, 10000)
los_angeles.add(houston, 1374)
los_angeles.add(phoenix, 357)
los_angeles.add(salt_lake_city, 579)

# Chicago valid destinations
chicago.add(new_york, 713)
# chicago.add(los_angeles, 10000)
chicago.add(chicago, 0)
chicago.add(minneapolis, 355)
chicago.add(denver, 920)
chicago.add(dallas, 803)
# chicago.add(seattle, 10000)
chicago.add(boston, 851)
# chicago.add(san_francisco, 10000)
chicago.add(st_louis, 262)
chicago.add(houston, 940)
# chicago.add(phoenix, 10000)
# chicago.add(salt_lake_city, 10000)

# Minneapolis valid destinations
minneapolis.add(new_york, 1018)
# minneapolis.add(los_angeles, 10000)
minneapolis.add(chicago, 355)
minneapolis.add(minneapolis, 0)
minneapolis.add(denver, 700)
# minneapolis.add(dallas, 10000)
minneapolis.add(seattle, 1395)
minneapolis.add(boston, 1123)
# minneapolis.add(san_francisco, 10000)
minneapolis.add(st_louis, 466)
# minneapolis.add(houston, 10000)
# minneapolis.add(phoenix, 10000)
minneapolis.add(salt_lake_city, 987)

# Denver valid destinations
# denver.add(new_york, 10000)
denver.add(los_angeles, 831)
denver.add(chicago, 920)
denver.add(minneapolis, 700)
denver.add(denver, 0)
denver.add(dallas, 663)
denver.add(seattle, 1021)
denver.add(san_francisco, 949)
denver.add(st_louis, 796)
denver.add(houston, 879)
denver.add(phoenix, 586)
denver.add(salt_lake_city, 371)

# Dallas valid destinations
dallas.add(new_york, 1374)
dallas.add(los_angeles, 1240)
dallas.add(chicago, 803)
# dallas.add(minneapolis, 10000)
dallas.add(denver, 663)
dallas.add(dallas, 0)
# dallas.add(seattle, 10000)
# dallas.add(boston, 10000)
# dallas.add(san_francisco, 10000)
dallas.add(st_louis, 547)
dallas.add(houston, 225)
dallas.add(phoenix, 887)
dallas.add(salt_lake_city, 999)

# Seattle valid destinations
# seattle.add(new_york, 10000)
seattle.add(los_angeles, 959)
# seattle.add(chicago, 10000)
seattle.add(minneapolis, 1395)
seattle.add(denver, 1021)
# seattle.add(dallas, 10000)
seattle.add(seattle, 0)
# seattle.add(boston, 10000)
seattle.add(san_francisco, 678)
# seattle.add(st_louis, 10000)
# seattle.add(houston, 10000)
seattle.add(phoenix, 1114)
seattle.add(salt_lake_city, 701)

# Boston valid destinations
boston.add(new_york, 213)
# boston.add(los_angeles, 10000)
boston.add(chicago, 851)
boston.add(minneapolis, 1123)
# boston.add(denver, 10000)
# boston.add(dallas, 10000)
# boston.add(seattle, 10000)
boston.add(boston, 0)
# boston.add(san_francisco, 10000)
boston.add(st_louis, 1038)
# boston.add(houston, 10000)
# boston.add(phoenix, 10000)
# boston.add(salt_lake_city, 10000)

# San Francisco valid destinations
# san_francisco.add(new_york, 10000)
san_francisco.add(los_angeles, 403)
# san_francisco.add(chicago, 10000)
# san_francisco.add(minneapolis, 10000)
san_francisco.add(denver, 949)
# san_francisco.add(dallas, 10000)
san_francisco.add(seattle, 678)
# san_francisco.add(boston, 10000)
san_francisco.add(san_francisco, 0)
# san_francisco.add(st_louis, 10000)
san_francisco.add(houston, 1645)
san_francisco.add(phoenix, 653)
san_francisco.add(salt_lake_city, 600)

# St. Louis valid destinations
st_louis.add(new_york, 875)
# st_louis.add(los_angeles, 10000)
st_louis.add(chicago, 262)
st_louis.add(minneapolis, 466)
st_louis.add(denver, 796)
st_louis.add(dallas, 547)
# st_louis.add(seattle, 10000)
st_louis.add(boston, 1038)
# st_louis.add(san_francisco, 10000)
st_louis.add(st_louis, 0)
st_louis.add(houston, 679)
st_louis.add(phoenix, 1272)
st_louis.add(salt_lake_city, 1162)

# H-Tine valid destinations
# houston.add(new_york, 10000)
houston.add(los_angeles, 1374)
houston.add(chicago, 940)
# houston.add(minneapolis, 10000)
houston.add(denver, 879)
houston.add(dallas, 225)
# houston.add(seattle, 10000)
# houston.add(boston, 10000)
houston.add(san_francisco, 1645)
houston.add(st_louis, 679)
houston.add(houston, 0)
# houston.add(phoenix, 10000)
houston.add(salt_lake_city, 1200)

# Phoenix valid destinations
phoenix.add(los_angeles, 357)
phoenix.add(denver, 586)
phoenix.add(dallas, 887)
phoenix.add(seattle, 1114)
phoenix.add(san_francisco, 653)
phoenix.add(st_louis, 1272)
phoenix.add(phoenix, 0)
phoenix.add(salt_lake_city, 504)

# Salt Lake City valid destinations
# salt_lake_city.add(new_york, 10000)
salt_lake_city.add(los_angeles, 579)
# salt_lake_city.add(chicago, 10000)
salt_lake_city.add(minneapolis, 987)
salt_lake_city.add(denver, 371)
salt_lake_city.add(dallas, 999)
salt_lake_city.add(seattle, 701)
# salt_lake_city.add(boston, 10000)
salt_lake_city.add(san_francisco, 600)
salt_lake_city.add(st_louis, 1162)
salt_lake_city.add(houston, 1200)
salt_lake_city.add(phoenix, 504)
salt_lake_city.add(salt_lake_city, 0)

# Finally define the search algorithm(s)
def a_star(start, goal):
    OPEN = dict()
    OPEN[start] = (start.getDistance(start) + geodesic(start.coordinates, goal.coordinates).miles)
    CLOSED = dict()

    while len(OPEN) > 0:
        keys = list(OPEN.keys())
        min = OPEN[keys[0]]
        city = keys[0]
        for x in OPEN:
            if OPEN[x] < min:
                city = x
                min = OPEN[x]
        CLOSED[city] = OPEN[city]
        if city == goal:
            print("Goal found!")
            solution = list()
            solution.insert(0, goal)
            CLOSED.pop(goal)
            while start not in CLOSED:
                keys = list(CLOSED.keys())
                min = keys[0]
                for x in CLOSED:
                    if (CLOSED[x] < CLOSED[min] and solution[0] in CLOSED[x].vertices):
                        min = x
                solution.insert(0, min)
                CLOSED.pop(min)
                
            for x in CLOSED:
                print(x, CLOSED[x])
            for city in solution:
                print(city)
            return solution
        else:
            print("City:", city)
            for destination in city.vertices:
                print("-", destination)
                if destination not in OPEN or destination not in CLOSED:
                    OPEN[destination] = (city.getDistance(destination) + geodesic(destination.coordinates, goal.coordinates).miles)
        OPEN.pop(city)
        print("\n")
    return "FAILURE"

if __name__ == "__main__":
    print("Problem 4 Solution")
    # Take user's input for the starting city.
    while (True):
        printChoices(graph)
        print("Which choice (#) would you like to choose as your starting point.")
        start_destination = input("Selection: " )
        if (start_destination.isdigit() and int(start_destination) in range(len(graph))):
            start_destination = int(start_destination)
            break
        else:
            print("Invalid Option. Please try again.")
    # Take user's input for the ending city.
    while (True):
        printChoices(graph)
        print("Which choice (#) would you like to choose as your ending point")
        ending_destination = input("Selection: ")
        if (ending_destination.isdigit() and int(start_destination) in range(len(graph)) and int(ending_destination) != int(start_destination)):
            ending_destination = int(ending_destination)
            break
        else:
            print("Invalid Option. Please try again.")
    # Reiterate the choices
    print("Calculating the distance from", graph[start_destination], "to", graph[ending_destination], "by using the A* algorithm.")
    path = a_star(graph[start_destination], graph[ending_destination])
    # print(path)