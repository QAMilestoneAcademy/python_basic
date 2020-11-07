# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

s=turtle.Screen()
s.bgcolor('black')
t = turtle.Pen()
t.speed('fastest')
for x in range(360):
    t.pencolor(colors[x%6])
    # t.pensize(x/100 + 1)
    t.forward(x)
    t.left(59)
s.exitonclick()
