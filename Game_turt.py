# Python Turtle Program
import turtle

shelly = turtle.Turtle()
shelly.shape('turtle')

# Coloring the Turtle
shelly.begin_fill()
colors = ["red", "green", "blue"]
shelly.color(colors[1])

# Move the Turtle Using the FOR Loop - Outer Loop Repeats the Square 6 Times
for n in range(6):
    # Inner Loop Repeat 4 Times To Make a Square
    for i in range(4):
        shelly.forward(100)
        shelly.left(90)
    # Add a Turn Before the Next Square
    shelly.right(60)

shelly.end_fill()
