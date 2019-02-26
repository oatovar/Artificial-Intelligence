#!/usr/bin/env python3
class City:
    def __init__(self, name):
        self.name = name
        self.coordinates = {}
        self.vertices = dict()

    def __str__(self):
        return self.name

    def add(self, vertice, distance):
        self.vertices[vertice] = distance
    
    def remove(self, vertice):
        self.vertices.pop(vertice)
def printChoices(graph):
    for index, city in enumerate(graph):
        print(index, ":", city)
# Cities that are allowed within program.
new_york = City("New York")
los_angeles = City("Los Angeles")
chicago = City("Chicago")
minneapolis = City("Minneapolis")
denver = City("Denver")
dallas = City("Dallas")
seattle = City("Seattle")
boston = City("Boston")
san_francisco = City("San Francisco")
st_louis = City("St. Louis")
houston = City("Houston")
phoenix = City("Phoneix")
salt_lake_city = City("Salt Lake City")

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
    print("Calculating the distance from", graph[start_destination], "to", graph[ending_destination])