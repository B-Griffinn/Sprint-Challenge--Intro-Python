# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.


class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    # TODO
    def drive(self):
        return "vroooom"

    def __str__(self):
        return f"The Ground Vehicle has {self.num_wheels} wheels and goes {self.drive()}."


# gv1 = GroundVehicle(2.5)
# print(gv1.drive())
# print(gv1.num_wheels)

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO
class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        super().__init__(num_wheels)

    def drive(self):
        return "BRAAAP!!"

    def __str__(self):
        return f"The Motorcycle has {self.num_wheels} wheels and goes {self.drive()}."


# m1 = Motorcycle(10)
# print(m1.num_wheels)
# print(m1.drive())

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO
for i in vehicles:
    print(i.drive())
