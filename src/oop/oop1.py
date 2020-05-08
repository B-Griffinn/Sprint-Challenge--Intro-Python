# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    ''' BASE Class aka Parent '''
    pass


class FlightVehicle(Vehicle):
    ''' subclass of vehicle  '''
    pass


class Starship(FlightVehicle):
    ''' subclass of FlightVehicle inherits all the way up to Vehicle '''
    pass


class GroundVehicle(Vehicle):
    ''' subclass of Vehicle '''
    pass


class Car(GroundVehicle):
    ''' subclass of GroundVehicle - inherits all the way up to Vehicle '''
    pass


class Motorcycle(GroundVehicle):
    ''' subclass of GroundVehicle - inherits all the way up to Vehicle '''
    pass


class Airplane(FlightVehicle):
    ''' subclass of FlightVehicle - inherits all the way up to Vehicle '''
    pass
