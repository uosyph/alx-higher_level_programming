#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        try:
            self.position = position
        except TypeError as typ:
            print(typ)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            self.__position = None
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.position:
            if self.size > 0:
                print('\n' * self.position[1], end="")
                for _ in range(self.__size):
                    print(' ' * self.position[0], end="")
                    print('#' * self.size)
        if self.__size == 0:
            print()

    def __str__(self):
        if self.__size == 0:
            return ''
        lenght = self.position[0] + self.size
        spaces = self.position[0]
        deep = self.position[1]
        for _ in range(deep):
            print()
        for _ in range(self.size - 1):
            for i in range(lenght):
                if i < spaces:
                    print("{}".format(" "), end="")
                else:
                    print("{}".format("#"), end="")
            print()
        return ' ' * self.position[0] + '#' * self.size
