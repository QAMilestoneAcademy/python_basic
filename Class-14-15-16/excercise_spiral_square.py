# Python program to draw
# Spiral Square Outside In and Inside Out
# using Turtle Programming
import turtle
s = turtle.Screen()
s.bgcolor("light green")
s.title("Spiral Square")
t = turtle.Turtle()
t.pen(pencolor="blue", fillcolor="yellow", pensize=10, speed=9)

t.begin_fill()
size=100
while size<=300:
    for i in range(0,4):
        t.fd(size)
        t.rt(90)
        size = size + 25
t.end_fill()
s.exitonclick()



