#!/usr/bin/python3
"""Class Rectangle inherits from Base class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes class constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Returns the area of the rectangle"""

        return self.__width * self.__height

    def display(self):
        """Prints the rectangle to the stdout"""

        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Returns the string representation of the rectangle"""

        a, d, e = self.id, self.width, self.height
        b, c = self.x, self.y
        return f"[Rectangle] ({a}) {b}/{c} - {d}/{e}"

    @property
    def width(self):
        """Returns the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the property of the width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the property of the height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    def update(self, *args, **kwargs):
        """Arguments for the rectangle"""

        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.__width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            if len(args) == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        else:
            for key, values in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, values)

    @property
    def x(self):
        """Returns x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets y positional attribute"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Returns y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Sets y positional attribute"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def to_dictionary(self):
        """Returns dictionary representation of the rectangle"""

        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
