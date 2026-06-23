import turtle

class FacePart:
    """Base class for all facial features relative to a center point."""
    def __init__(self, t, center_x=0, center_y=0):
        self.t = t
        self.center_x = center_x
        self.center_y = center_y

    def move_to(self, rel_x, rel_y):
        """Helper method to lift pen and move relative to the center origin."""
        self.t.penup()
        self.t.goto(self.center_x + rel_x, self.center_y + rel_y)
        self.t.pendown()

class FaceOutline(FacePart):
    """Draws the main shape of the face."""
    def draw(self):
        # Move down by radius (150) to keep (0,0) as the geometric center
        self.move_to(0, -150)
        self.t.pensize(5)
        self.t.pencolor("black")
        self.t.fillcolor("pink") # Funky color
        self.t.begin_fill()
        self.t.circle(150)
        self.t.end_fill()

class Eyes(FacePart):
    """Draws a pair of eyes symmetric about the center line."""
    def draw(self):
        self.t.pensize(3)
        self.t.pencolor("black")
        
        # Left Eye
        self.move_to(-50, 40)
        self.t.fillcolor("white")
        self.t.begin_fill()
        self.t.circle(25)
        self.t.end_fill()
        
        # Left Pupil
        self.move_to(-50, 55)
        self.t.fillcolor("black") # Funky pupil
        self.t.begin_fill()
        self.t.circle(10)
        self.t.end_fill()

        # Right Eye
        self.move_to(50, 40)
        self.t.fillcolor("white")
        self.t.begin_fill()
        self.t.circle(25)
        self.t.end_fill()
        
        # Right Pupil
        self.move_to(50, 55)
        self.t.fillcolor("black")
        self.t.begin_fill()
        self.t.circle(10)
        self.t.end_fill()

class Nose(FacePart):
    """Draws a triangular nose centered horizontally."""
    def draw(self):
        self.move_to(0, 20)
        self.t.pensize(4)
        self.t.pencolor("black")
        self.t.fillcolor("coral") # Funky color
        self.t.begin_fill()
        
        # Draw triangle relative to the nose starting position
        self.t.goto(self.center_x - 20, self.center_y - 20)
        self.t.goto(self.center_x + 20, self.center_y - 20)
        self.t.goto(self.center_x + 0, self.center_y + 20)
        
        self.t.end_fill()

class Mouth(FacePart):
    """Draws a smiling mouth curve."""
    def draw(self):
        self.move_to(-60, -40)
        self.t.pensize(6)
        self.t.pencolor("black")
        self.t.setheading(-60) # Angle downward to start the smile arc
        self.t.circle(70, 120) # Draw a 120-degree arc
        self.t.setheading(0)   # Reset heading angle

class FunkyFaceApp:
    """Main application orchestrator class."""
    def __init__(self):
        # Set up window screen
        self.screen = turtle.Screen()
        self.screen.title("OOP Funky Face")
        self.screen.bgcolor("turquoise") # Funky background color
        
        # Set up drawing turtle
        self.t = turtle.Turtle()
        self.t.speed(3)
        
        # Shared fixed center coordinates
        self.origin_x = 0
        self.origin_y = 0

    def run(self):
        # Instantiate object composition structure
        face = FaceOutline(self.t, self.origin_x, self.origin_y)
        eyes = Eyes(self.t, self.origin_x, self.origin_y)
        nose = Nose(self.t, self.origin_x, self.origin_y)
        mouth = Mouth(self.t, self.origin_x, self.origin_y)
        
        # Draw everything in sequence
        face.draw()
        eyes.draw()
        nose.draw()
        mouth.draw()
        
        # Hide turtle and complete program loop
        self.t.hideturtle()
        self.screen.mainloop()

# Run the program
if __name__ == "__main__":
    app = FunkyFaceApp()
    app.run()


