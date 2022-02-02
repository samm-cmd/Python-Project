# make a house
# Import turtle module
import turtle
turtle.bgcolor('pink')
shelly = turtle.Turtle()

# Make the first Big Square for the House
shelly.begin_fill()
shelly.color('gray')

# FOR LOOP
for i in range(4):
    shelly.forward(100)
    shelly.left(90)
shelly.end_fill()
shelly.penup()
shelly.goto(-20, 100)
shelly.pendown()

# Make a Red Triangle Roof
shelly.begin_fill()
shelly.color('red')
shelly.left(60)
shelly.forward(140)
shelly.right(120)
shelly.forward(140)
shelly.right(120)
shelly.forward(140)
shelly.end_fill()

# Make a window
shelly.penup()
shelly.goto(25, 80)
shelly.pendown()
shelly.begin_fill()
shelly.color('yellow')

# FOR Loop
for n in range(4):
    shelly.forward(20)
    shelly.left(90)
shelly.end_fill()
