#!/usr/bin/python3

"""
    I am making a collection of files to
    build the rectangle class,
    in order to print a rectangle at the
    end of the project.
"""


class Rectangle:

    """
        This is the class of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """
            Let's make a rectangle.

            Args:

                width (int)
                height (int)
        """

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        "property to give the width of the rectangle's shape"
        return self.__width

    @width.setter
    def width(self, value):
        """
        objective is to get the value of width

        Args:
             value
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        objective here is to get value of height

        Args:
            value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Will return the area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Will return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """Return the rectangle made as a string made of symbols #"""
        if self.width == 0 or self.height == 0:
            return ""

        rect_lines = []
        for _ in range(self.height):
            rect_lines.append(str(self.print_symbol) * self.width)

        return "\n".join(rect_lines)

    def __repr__(self):
        """Return string representation to create a new instance"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a specific msg when the instance is deleted"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """
        Will return the biggest rectangle based
        on the area after comparison between 2 rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
