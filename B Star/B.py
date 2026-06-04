import turtle

# Set up the canvas background color
turtle.Screen().bgcolor("lightblue")
board = turtle.Turtle()

# --- FIRST TRIANGLE FOR STAR ---
board.forward(100) # draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

# Move the turtle to the starting position for the second triangle
board.penup()
board.right(150)
board.forward(50)

# --- SECOND TRIANGLE FOR STAR ---
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)
board.clear()

# --- FIRST TRIANGLE FOR STAR ---
board.forward(100) # draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

# Move the turtle to the starting position for the second triangle
board.penup()
board.right(150)
board.forward(50)

# --- SECOND TRIANGLE FOR STAR ---
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)
board.clear()

# --- FIRST TRIANGLE FOR STAR ---
board.forward(100) # draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

# Move the turtle to the starting position for the second triangle
board.penup()
board.right(150)
board.forward(50)

# --- SECOND TRIANGLE FOR STAR ---
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

# Keep the window open when finished
turtle.done()