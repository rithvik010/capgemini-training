import math
from abc import ABC, abstractmethod
class Ishape(ABC):
    @abstractmethod
    def Calculate_area(self):
        pass
class Rectangle(Ishape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def Calculate_area(self):
        return self.length*self.width
class Circle(Ishape):
    def __init__(self,radius):
        self.radius=radius
    def Calculate_area(self):
        return math.pi*self.radius*self.radius
circle_area=Circle(5)
print(f"Area of Circle= {circle_area.Calculate_area():.2f} square units")
rectangle_area=Rectangle(5,6)
print(f"Area of ractangle= {rectangle_area.Calculate_area()} square units")
