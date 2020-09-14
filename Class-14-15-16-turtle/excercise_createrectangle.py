# Rectangle
# Fd 300 rt 90 fd 150 rt 90
# Fd 300 rt 90 fd 150 rt 90
import turtle
import time
s = turtle.Screen()
s.bgcolor("light blue")
t=turtle.Turtle()
t.pen(pencolor="red", fillcolor="purple", pensize=10, speed=2)
t.begin_fill()
t.fd(200)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(100)
t.end_fill()
time.sleep(5)

