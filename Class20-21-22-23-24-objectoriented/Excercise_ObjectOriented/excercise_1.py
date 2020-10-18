# Exercise Question 1: Create a Vehicle class with name of vehicle,
# max_speed and mileage instance attributes

class Vehicle:
    def __init__(self,name, max_speed, mileage):
        self.name=name
        self.max_speed = max_speed
        self.mileage = mileage

vehicle1 = Vehicle("Volvo",240, 18)
print(vehicle1.max_speed, vehicle1.mileage)