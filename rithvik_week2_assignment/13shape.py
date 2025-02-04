class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return (self.side_length ** 2)
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return (0.5*self.base*self.height)
square=Square(5)
print(f"Area of Square ={square.area()}")
