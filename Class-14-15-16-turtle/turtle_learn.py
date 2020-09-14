#import turtle -inbuilt library
import turtle
import time
#open the turtle screen
s = turtle.Screen()
# #set background color
s.bgcolor("light green")
# # # This window is called the screen. It’s where you can view the output of your code. The little black triangular shape in the middle of the screen is called the turtle.
# time.sleep(5)
# # # Next, you initialize the variable t, which you’ll then use throughout the program to refer to the turtle
t=turtle.Turtle()

# # The first thing you’ll learn when it comes to programming with the Python turtle library is how to make the turtle move in the direction you want it to go.
#
# # There are four directions that a turtle can move in:
# #
# # Forward
# # Backward
# # Left
# # Right
#
# # When you run these commands, the turtle will turn right by ninety degrees, go forward by a hundred units, turn left by ninety degrees, and move backward by a hundred units. You can see how this looks in the image below:
# #shortended t.rt()
t.right(90)
# # shortended t.fd()
t.forward(100)
# # # t.lt()
t.left(90)

# # # t.bk()
t.backward(100)
time.sleep(5)
# # #go to any coordinate with below
# # t.goto(100,100)
# # # To bring the turtle back to its home position, you type the following:
# t.home()
# # Changing the Pen Speed
# # The turtle generally moves at a moderate pace. If you want to decrease or increase the speed to make your turtle move slower or faster, then you can do so by typing the following:
# t.speed(1)
# t.fd(100)
# t.speed(5)
# t.rt(60)
# #customize turtle
# t.pen(pencolor="red", fillcolor="purple", pensize=10, speed=9)
# time.sleep(2)
#
# ##Filling an image
# t.begin_fill()
# t.circle(90)
# t.end_fill()
# time.sleep(2)
#
# t.done()