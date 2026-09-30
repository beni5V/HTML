#Part 1-IMPORT
import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Graphics")

#Part 2-CREATE TURTLE OBJECT
board = turtle.Turtle()
#board.speed()
board.hideturtle()

#Part 3- OUTER COLOR SPRIAL
colors = ["cyan","magenta", "yellow", "white", "orange", "green", "red", "golden", "purple", "pink","violet", "lime", "teal", "indigo", "gold", "silver", "brown", "maroon", "olive", "navy"]
for i in range(1000):
    board.color(colors[i % len(colors)])
    board.width(6)
    board.forward(i * 2)
    board.left(91)

#Part 4-PEN CONTROL
board.penup()   #Pen up to draw.
board.goto(0, -60)
board.setheading(90)
board.pendown()  #Pen down to stop drawing.
board.color("gold","white")
board.begin_fill()
for i in range(5):
    board.forward(130)
    board.right(144)
board.end_fill()

#Part 5-INNER COLOR SPRIAL
board.penup()
board.goto(0,0)
board.pendown()
petal_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for i in range(36):
    board.color(petal_colors[i % len(petal_colors)],
                petal_colors[(i+2) % len(petal_colors)])
    board.begin_fill()
    for j in range(4):
        board.forward(55)
        board.right(90)
    board.end_fill()
    board.right(10)