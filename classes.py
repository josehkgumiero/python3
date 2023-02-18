class Rectangle:
    
    def __init__(self, width, height):
        self._width = width
        self.height = height
    
    def area(self):
        return self._width * self.height

    def perimeter(self):
        return 2 * (self._width + self.height)

    def __str__(self):
        return 'Rectangle: _width={0} height={1}'.format(self._width, self.height)

    def __repr__(self):
        return 'Rectangle({0},{1})'.format(self._width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self.height == other.height
        else:
            return False
    
    def get__width(self):
        return self._width

    def set_width(self, width):
        if width < 0:
            raise ValueError('Width must be positive.')
        else:
            self._width = width

r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)

print(r1._width)
print(r1.height)
print(r1.area())
print(r1.perimeter())
print(str(r1))
print(r1)
print(r1 is not r2)
print(r1 == r2)
print(r1 == 100)