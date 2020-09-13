import turtle
import time

t=turtle.Turtle()

turtle.bgcolor("yellow")
t.pencolor("green")

for i in range(50,100,10):
  t.circle(i)


time.sleep(10)