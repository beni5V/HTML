import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    try:
        user_radius = float(input("Enter the radius of the circle: "))

        if user_radius < 0:
            print("Radius cannot be negative.")
        else:
            my_circle = Circle(user_radius)
            print(f"Area of the circle: {my_circle.calculate_area():.2f}")
            print(f"Perimeter of the circle: {my_circle.calculate_perimeter():.2f}")

    except ValueError:
        print("Please enter a valid numeric value.")
