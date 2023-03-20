'''
-----------------------------------
   File: shapes.py
Project: Turtle Shapes and Movement
 Author: Vexnos
   Date: 2023-03-20
-----------------------------------
'''
#-------Libraries-------
import turtle # Import the turtle library

#-------Functions-------
# Turtle Polygons
class Polygon:
    def __init__(self, sides, name, distance):
        self.sides = sides
        self.name = name
        self.distance = distance
        self.interior_angle = (self.sides - 2) * 180
        self.angle = self.interior_angle / self.sides

    def draw(self):
        vex.begin_fill()
        for i in range(self.sides):
            vex.forward(self.distance)
            vex.right(180 - self.angle)
        vex.end_fill()

# Turtle Movement
class Movement:
    def __init__(self, keybind, heading):
        self.keybind = keybind
        self.heading = heading

    def move(self):
        vex.setheading(self.heading)
        vex.forward(50)

# Close function
def close():
    wn.bye()

# Raises Turtle Pen
def pen_up():
    vex.penup()

# Turtle Pen Falls
def pen_down():
    vex.pendown()

def user_input():
    shapes = {
        "triangle": triangle,
        "square": square,
        "pentagon": pentagon,
        "hexagon": hexagon,
        "heptagon": heptagon,
        "octagon": octagon,
        "nonagon": nonagon,
        "decagon": decagon,
        "dodecagon": dodecagon,
        "circle": circle
    }
    print(", ".join(list(shapes)))
    validating = True
    while validating:
        shape = input("Please pick a shape from this list: ")

        if shape.lower() in shapes:
            return shapes[shape]
        print("Invalid shape listed! Please try agian.")

#-------Main-Routine-------
if __name__ == "__main__":
    looping = True
    while looping:
        # Define shapes
        triangle = Polygon(3, "Triangle", 50)
        square = Polygon(4, "Square", 50)
        pentagon = Polygon(5, "Pentagon", 50)
        hexagon = Polygon(6, "Hexagon", 50)
        heptagon = Polygon(7, "Heptagon", 50)
        octagon = Polygon(8, "Octagon", 50)
        nonagon = Polygon(9, "Nonagon", 50)
        decagon = Polygon(10, "Decagon", 50)
        dodecagon = Polygon(12, "Dodecagon", 50)
        circle = Polygon(500, "Circle", 1)

        shape = user_input()

        # Turtle Setup
        wn = turtle.Screen() # Define the screen as a variable
        wn.setup(500, 400) # Setup the screen resolution
        wn.bgcolor("darkblue") # Set the background color
        wn.title("Titled Document") # Set the screen title
        vex = turtle.Turtle() # Define the turtle into a variable
        vex.color("white") # Set the turtle color
        vex.width(3) # Set the turtle width

        # Draw the Shape
        shape.draw()

        # Define class Movement for each direction
        right = Movement("d", 0)
        up = Movement("w", 90)
        left = Movement("a", 180)
        down = Movement("s", 270)

        # Listen for Keybinds
        wn.listen()
        wn.onkey(close, "q")
        wn.onkey(right.move, "d")
        wn.onkey(up.move, "w")
        wn.onkey(left.move, "a")
        wn.onkey(down.move, "s")
        wn.onkey(pen_up, "r")
        wn.onkey(pen_down, "f")

        # Don't quit when finished
        wn.mainloop()

        # Allow the user to repeat the program
        draw_again = input("Do you want to draw another shape? (y/n): ").lower()
        looping = draw_again.startswith("y")
