import turtle

# Create turtle
t = turtle.Turtle()
t.speed(3)

# Draw Triangle
t.penup()
t.goto(-200, 100)
t.pendown()

for i in range(3):
    t.forward(100)
    t.left(120)

# Draw Rectangle
t.penup()
t.goto(0, 100)
t.pendown()

for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)

# Draw Square
t.penup()
t.goto(-200, -100)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(90)

# Draw Circle
t.penup()
t.goto(50, -150)
t.pendown()

t.circle(50)

# Finish
turtle.done()