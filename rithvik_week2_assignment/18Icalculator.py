from abc import ABC ,abstractmethod
class Icalculator(ABC):
    def add(self):
        pass
    def subtract(self):
        pass
    def multiply(self):
        pass
    def divide(self):
        pass
class BasicCalculator(Icalculator):
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(sel,a,b):
        if b!=0:
            return a/b
calculator=BasicCalculator()
print(f"Addition:{calculator.add(3,5)}")
print(f"Subtraction:{calculator.subtract(5,5)}")
print(f"Multiplication:{calculator.multiply(5,9)}")
print(f"Division:{calculator.divide(5,1)}")