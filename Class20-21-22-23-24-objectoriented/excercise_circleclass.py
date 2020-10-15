# Create a Circle class and intialize it with radius.
# Make two methods getArea and getCircumference inside this class.
#Create an object of circle class and print area & circumference for a given radius

class Circle():
  def __init__(self,radius):
    self.radius = radius
  def  getArea(self):
    return 3.14*self.radius*self.radius
  def getCircumference(self):
    return self.radius*2*3.14