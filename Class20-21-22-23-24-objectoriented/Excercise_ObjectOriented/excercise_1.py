# Exercise Question 1: Create a Vehicle class with name of vehicle,
# max_speed and mileage instance attributes

class Vehicle:
    def __init__(self,name, max_speed, mileage):
        self.name=name
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle("Volvo",240, 18)
print(modelX.max_speed, modelX.mileage)