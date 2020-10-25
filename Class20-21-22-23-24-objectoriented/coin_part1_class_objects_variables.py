class Pound:
    value = 1.0
    color = "gold"
    num_edges = 1
    diameter = 22.5  # in millimeter
    thicknes = 3.15  # in mm
    heads = True

coin1=Pound()
# print(type(coin1))
print(coin1.color)
coin1.color="green"
print(coin1.color)

coin2=Pound()
print(coin2.color)


#
# coin1=Pound()
# print(coin1.color)
# print(coin1.value)
# coin1.color="green"
# print(coin1.color)
#
# coin2=Pound()
# print(coin2.color)
# print(coin2.value)
