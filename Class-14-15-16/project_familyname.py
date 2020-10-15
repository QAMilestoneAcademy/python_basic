import turtle
s=turtle.Screen()
t=turtle.Turtle()
s.bgcolor("white")
t.speed(9)

colors = ["red", "yellow", "blue", "green", "orange",
        "purple", "white", "brown", "gray", "pink" ]

family = []

name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")

while name != "":

    family.append(name)
    name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")

for x in range(70):
    t.pencolor(colors[x%len(family)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)], font = ("Arial", int((x+8)/4), "bold") )
    t.left(360/len(family)+2)

s.exitonclick()
# #
