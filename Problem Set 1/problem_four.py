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
graph = dict()

graph[new_york] = ""

if __name__ == "__main__":
    print("Problem 4 Solution")
    print("Which city would you like to choose as your starting point.")
    for index, city in enumerate(graph):
        print(index, ":", city)