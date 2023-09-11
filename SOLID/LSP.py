class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def area(self):
        return self.width * self.height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def calculate_area(rectangle: Rectangle):
    width = rectangle.width
    rectangle.height = 10
    expected = int(width*10)
    print(f'Expected an area of {expected}, got {rectangle.area}')


rc = Rectangle(2, 3)
calculate_area(rc)
