class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
    def details(self):
        return f"Name:{self.name}\nRoll Number :{self.roll_number}"
student1=Student("Luffy","R01")
print(student1.details())