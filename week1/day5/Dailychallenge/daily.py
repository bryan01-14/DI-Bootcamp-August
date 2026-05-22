"""Circle class with dunder methods and optional Turtle visualization."""

import math




class Circle:
    """A class to represent a circle."""

    def __init__(self, radius=None, diameter=None):
        """
        Initialize a Circle using either radius or diameter.
        - If radius is provided, use it directly.
        - If diameter is provided, compute radius from it.
        - If neither is provided, raise a ValueError.
        """
        if radius is not None:
            if radius <= 0:
                raise ValueError("Radius must be a positive number.")
            self.radius = radius
        elif diameter is not None:
            if diameter <= 0:
                raise ValueError("Diameter must be a positive number.")
            self.radius = diameter / 2
        else:
            raise ValueError("You must provide either a radius or a diameter.")



    @property
    def diameter(self):
        """Return the diameter of the circle."""
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        """Set the radius based on a given diameter."""
        if value <= 0:
            raise ValueError("Diameter must be a positive number.")
        self.radius = value / 2



    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2


    def __str__(self):
        """Return a user-friendly string representation of the circle."""
        return (
            f"Circle(radius={self.radius:.2f}, "
            f"diameter={self.diameter:.2f}, "
            f"area={self.area():.2f})"
        )

    def __repr__(self):
        """Return an unambiguous string representation of the circle."""
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        """
        Add two circles together.
        Returns a new Circle with the combined radius.
        """
        if not isinstance(other, Circle):
            raise TypeError("Can only add a Circle to another Circle.")
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        """
        Check if this circle is greater than another.
        Returns True if self.radius > other.radius.
        """
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with another Circle.")
        return self.radius > other.radius

    def __lt__(self, other):
        """
        Check if this circle is less than another.
        Returns True if self.radius < other.radius.
        """
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with another Circle.")
        return self.radius < other.radius

    def __eq__(self, other):
        """
        Check if two circles are equal.
        Returns True if both have the same radius.
        """
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with another Circle.")
        return self.radius == other.radius

    def __ge__(self, other):
        """Check if this circle is greater than or equal to another."""
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        """Check if this circle is less than or equal to another."""
        return self.__lt__(other) or self.__eq__(other)




def draw_circles_with_turtle(circles):
    """
    Draw sorted circles visually using the Turtle module.
    Circles are drawn left to right, sorted by radius.
    """
    try:
        import turtle

        screen = turtle.Screen()
        screen.title("Sorted Circles - Turtle Visualization")
        screen.bgcolor("white")

        t = turtle.Turtle()
        t.speed(0)       # Fastest drawing speed
        t.hideturtle()

        sorted_circles = sorted(circles)
        colors = ["red", "blue", "green", "orange", "purple", "cyan"]

        # Starting x position
        x_offset = -300

        for i, circle in enumerate(sorted_circles):
            color = colors[i % len(colors)]
            t.penup()
            # Move to bottom of circle (turtle draws from bottom)
            t.goto(x_offset, -circle.radius)
            t.pendown()
            t.pencolor(color)
            t.circle(circle.radius)

            # Label the circle
            t.penup()
            t.goto(x_offset, -circle.radius - 20)
            t.write(
                f"r={circle.radius:.1f}",
                align="center",
                font=("Arial", 10, "normal")
            )

            # Move to the right for the next circle
            x_offset += circle.radius * 2 + 20

        screen.mainloop()

    except ImportError:
        print("\n  Turtle module not available. Skipping visualization.")
    except Exception as e:
        print(f"\n  Turtle error: {e}")




def main():
    """Main function to test the Circle class."""

    print("=" * 50)
    print("           CIRCLE CLASS TESTS")
    print("=" * 50)

    # Create circles using radius
    c1 = Circle(radius=5)
    c2 = Circle(radius=3)
    c3 = Circle(radius=7)
    c4 = Circle(radius=5)

    # Create circle using diameter
    c5 = Circle(diameter=10)  # radius = 5

    # --- __str__ and __repr__ ---
    print("\n--- __str__ ---")
    print(c1)
    print(c2)
    print(c3)

    print("\n--- __repr__ ---")
    print(repr(c1))

    # --- area ---
    print("\n--- Area ---")
    print(f"  Area of c1 (r=5): {c1.area():.2f}")
    print(f"  Area of c3 (r=7): {c3.area():.2f}")

    # --- diameter property ---
    print("\n--- Diameter ---")
    print(f"  c1 diameter: {c1.diameter}")
    print(f"  c5 (diameter=10) radius: {c5.radius}")

    # --- __add__ ---
    print("\n--- Addition ---")
    c_sum = c1 + c2
    print(f"  c1 + c2 = {c_sum}")

    # --- __gt__ ---
    print("\n--- Greater Than ---")
    print(f"  c1 (r=5) > c2 (r=3): {c1 > c2}")
    print(f"  c2 (r=3) > c1 (r=5): {c2 > c1}")

    # --- __lt__ ---
    print("\n--- Less Than ---")
    print(f"  c2 (r=3) < c1 (r=5): {c2 < c1}")
    print(f"  c3 (r=7) < c1 (r=5): {c3 < c1}")

    # --- __eq__ ---
    print("\n--- Equality ---")
    print(f"  c1 (r=5) == c4 (r=5): {c1 == c4}")
    print(f"  c1 (r=5) == c5 (diameter=10, r=5): {c1 == c5}")
    print(f"  c1 (r=5) == c2 (r=3): {c1 == c2}")

    # --- sorted list ---
    print("\n--- Sorted List ---")
    circles = [c3, c1, c2, c4]
    print("  Before sorting:")
    for c in circles:
        print(f"    {repr(c)}")

    sorted_circles = sorted(circles)
    print("  After sorting (ascending):")
    for c in sorted_circles:
        print(f"    {repr(c)}")

    sorted_desc = sorted(circles, reverse=True)
    print("  After sorting (descending):")
    for c in sorted_desc:
        print(f"    {repr(c)}")

    # --- Error handling ---
    print("\n--- Error Handling ---")
    try:
        bad = Circle()
    except ValueError as e:
        print(f"  ValueError: {e}")

    try:
        bad = Circle(radius=-3)
    except ValueError as e:
        print(f"  ValueError: {e}")

    # --- Bonus: Turtle ---
    print("\n--- Bonus: Turtle Visualization ---")
    print("  Drawing circles with Turtle (close window to continue)...")
    draw_circles_with_turtle([c1, c2, c3, Circle(radius=2), Circle(radius=9)])


if __name__ == "__main__":
    main()