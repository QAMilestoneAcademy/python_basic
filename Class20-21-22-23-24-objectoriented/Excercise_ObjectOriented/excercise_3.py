#Add Seating capacity method to vehicle class
# Create a Bus class that inherits from the Vehicle class.
# Give the capacity argument of Bus.seating_capacity() a default value of 50
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
            #f is similar to format method and variables are passed in curly brace place holders
            return f"The seating capacity of a {self.name} is {capacity} passengers"
            #return "The seating capacity of a {} is {} passengers".format(self.name,capacity)

class Bus(Vehicle):

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())