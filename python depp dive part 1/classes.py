class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

r1 = Rectangle(10,20)
print(r1.width)
r1.width = 100
print(r1.width)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_width(self):
        return self.width
    
    def set_width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive.")
        else:
            self.width = width
    
    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive.")
        else:
            self.width = width
    
    @property
    def height(self):
        return self.height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width * self.height)
    
    def to_string(self):
        return "Rectangle: width={0}, height={1}".format(self.width, self.height)

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.width, self.height)
    
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

r1 = Rectangle(10,20)
print(r1.area())
print(r1.perimeter())

print(str(r1))
print(r1.to_string())
print(r1)

r1 = Rectangle(10, 20)
r2 = Rectangle(10, 200)
print(r1 is not r2)
print(r1 == r2)

print(r1 < r2)