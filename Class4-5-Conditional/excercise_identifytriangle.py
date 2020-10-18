print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x==y and y==z and z==x:
    print("triangle is an equilateral triangle")
elif x==y or y==z or x==z:
    print("triangle is an isoceles triangle")
else:
    print("triangle is scalene triangle")


#
# if x+y>z and y+z >x and x+z>y:
#     if x == y == z:
#         print("Equilateral triangle")
#     elif x==y or y==z or z==x:
#         print("isosceles triangle")
#     else:
#         print("Scalene triangle")
# else:
#     print("Enter correct measurement of sides. Bye for now !")
