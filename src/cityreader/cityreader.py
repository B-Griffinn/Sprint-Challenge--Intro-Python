# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

import csv


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"{self.name}, {self.lat}, {self.lon}."


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list
    with open('cities.csv', 'r') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        next(read_csv)
        # loop through cities and append name, lat and lon
        for i in read_csv:
            cities.append(City((i[0]), float(i[3]), float(i[4])))

    return cities


cityreader(cities)

# # Print the list of cities (name, lat, lon), 1 record per line.
# for c in cities:
#     print(c)


# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
# user_input = two points, each specified by latitude and longitude
# split input and assign to variable which will be a list

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    # TODO Ensure that the lat and lon valuse are all floats
    # Go through each city and check to see if it falls within
    # the specified coordinates.

    # Hint: normalize the input data so that it's always one or the other, then search for cities.
    # lat1 needs to be <= lat of city
    # lat2 needs to be >= lat of city
    # lon1 needs to be <= lon of city
    # lon2 needs to be >= lon of city
    if (lat1 > lat2):
        lat2, lat1 = lat1, lat2
    if (lon1 > lon2):
        lon2, lon1 = lon1, lon2

    for i in cities:
        if i.lat >= lat1 and i.lat <= lat2 and i.lon >= lon1 and i.lon <= lon2:
            within.append(i)

    return within


# ask for users input twice to plot two points
user_input1 = input(
    "Please enter two points seperated by a space. Point 1: lat, Point 2: lon. ")
user_input2 = input(
    "Please enter another two points seperated by a space. Point 1: lat, Point 2: lon. ")

# set the user input to floats in order for our city search to work properly.
split_user_lat1 = float(user_input1.split(' ')[0])
split_user_lon1 = float(user_input1.split(' ')[1])
split_user_lat2 = float(user_input2.split(' ')[0])
split_user_lon2 = float(user_input2.split(' ')[1])

# just checeking my split values.
# print(split_user_lat1, split_user_lat2, split_user_lon1, split_user_lon2)

# create a loop that calls the city-stretch function and pass in its args
for x in cityreader_stretch(split_user_lat1, split_user_lon1,
                            split_user_lat2, split_user_lon2, cities):
    # we just want the city_name, lat, lon seperated by commas
    print(f"{x.name}, {x.lat}, {x.lon}")
