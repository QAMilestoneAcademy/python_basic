#giving behaviours to coins like rusting, fliping,cleaning & spending
import random
class Pound:
    #self is a parameter which refers to a specific instance of the class.For example if I create coin1 -self will be coin1 & similarly
    #defining constructor.It does not return anything.Helps to set up initial properties of an object
    def __init__(self,rare=False):
        self.rare=rare
        if self.rare:
           self.value=1.25
        else:
           self.value=1.00
        self.color="gold"
        self.num_edges=1
        self.diameter=22.5# in millimeter
        self.thicknes=3.15#in mm
        self.heads=True

    def rust(self):
         self.color="greenish"

    def clean(self):
        self.color="gold"

    def flip(self):
        heads_options=[True,False]
        choice=random.choice(heads_options)
        self.heads=choice

    def __del__(self):
        print("coin spent")

coin1=Pound(rare=True)
coin2=Pound()
print("coin1",coin1.value)
print("coin2",coin2.value)

print("coin1",coin1.color)

print("coin2",coin2.color)
#apply rust on coin1
coin1.rust()

print("coin1 rusted",coin1.color)

#apply clean on coin1
coin1.clean()

print("coin1 clean",coin1.color)
#coin before flip
print(coin1.heads)

coin1.flip()
print(coin1.heads)