print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x+y>z and y+z>x and x+z>y:
    if x==y and y==z and z==x:
        print("Triangle is an equilateral triangle")
    elif x==y or y==z or z==x:
        print("Triangle is an isoceles triangle")
    else:
        print("Triangle is a scalene triangle")
else:
    print("This will not create a triangle")