import turtle
s=turtle.Screen()
t=turtle.Turtle()
s.bgcolor("cyan")
t.pencolor("yellow")
t.width(10)
t.speed(9)
for i in range(50,100,20):
 t.circle(i)
s.exitonclick()


