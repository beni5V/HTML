import turtle

# PART 1 — SET UP THE CANVAS
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colour Loop Artwork")


# PART 2 — CREATE THE TURTLE
artist = turtle.Turtle()
artist.speed("fastest")
artist.hideturtle()
artist.pensize(2)

# PART 3 — DRAW A FILLED PETAL
def draw_petal(size, colour):
    artist.color(colour)
    artist.begin_fill()

    for _ in range(2):
        artist.circle(size, 60)
        artist.left(120)

    artist.end_fill()

# PART 4 — CREATE THE COLOUR LOOP ARTWORK
colors = ["cyan","magenta", "yellow", "white", "orange", "green", "red", "golden", "purple", "pink","violet", "lime", "teal", "indigo", "gold", "silver", "brown", "maroon", "olive", "navy"]
for i in range(1000):
    for i in range(36):
        draw_petal(90, colors[i % len(colors)])
        artist.right(10)

# PART 5 — DRAW A FILLED CENTRE CIRCLE
artist.penup()
artist.goto(0, -25)
artist.pendown()

artist.color("white")
artist.begin_fill()
artist.circle(25)
artist.end_fill()

# PART 6 — DRAW A STAR
def draw_star(x, y, size, colour):
    artist.penup()
    artist.goto(x, y)
    artist.setheading(0)
    artist.pendown()

    artist.color(colour)
    artist.begin_fill()

    for _ in range(5):
        artist.forward(size)
        artist.right(144)

    artist.end_fill()

# PART 7 — ADD STARS TO THE ARTWORK(My own addition)
draw_star(-230, 150, 35, "yellow")
draw_star(200, 150, 30, "cyan")
draw_star(-220, -150, 25, "magenta")
draw_star(210, -140, 35, "orange")

# PART 8 — DRAW SMALL CIRCLES
def draw_circle(x, y, size, colour):
    artist.penup()
    artist.goto(x, y)
    artist.pendown()

    artist.color(colour)
    artist.begin_fill()
    artist.circle(size)
    artist.end_fill()

draw_circle(-170, 80, 10, "white")
draw_circle(170, 70, 12, "yellow")
draw_circle(-160, -80, 8, "cyan")
draw_circle(160, -70, 10, "lime")

# PART 9 — DRAW DIAMOND SHAPES
def draw_diamond(x, y, size, colour):
    artist.penup()
    artist.goto(x, y)
    artist.setheading(45)
    artist.pendown()

    artist.color(colour)
    artist.begin_fill()

    for _ in range(4):
        artist.forward(size)
        artist.right(90)

    artist.end_fill()

draw_diamond(-120, 190, 20, "red")
draw_diamond(120, 190, 20, "blue")
draw_diamond(-130, -190, 18, "orange")
draw_diamond(130, -190, 18, "lime")

turtle.done()