# Python Program of a Turtle
import turtle

shelly = turtle.Turtle()
shelly.shape('turtle')

# Coloring the turtle
shelly.begin_fill()
colors = ["red", "green", "blue"]
shelly.color(colors[1])

# Move the turtle using the FOR loop - Outer Loop Repeats the Square 6 times
for n in range(6):
    # Inner Loop Repeat 4 times to make a square
    for i in range(4):
        shelly.forward(100)
        shelly.left(90)
    # Add a turn before the next square
    shelly.right(60)

shelly.end_fill()
