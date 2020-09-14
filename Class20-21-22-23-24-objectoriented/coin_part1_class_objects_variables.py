class Pound:
    value=1.0
    color="gold"
    num_edges=1
    diameter=22.5# in millimeter
    thicknes=3.15#in mm
    heads=True
coin1=Pound()
print(type(coin1))
print(coin1.value)
coin1.color="greenish"
print(coin1.color)
coin2=Pound()
print(coin2.color)

#classes are base templates an object is being made from.Actual objects can have there own state values, methods.All the objects from same class are independent of each other
#suppose green is more valuable
coin1.value=1.2
#so different objects can have different values
print(coin2.value)