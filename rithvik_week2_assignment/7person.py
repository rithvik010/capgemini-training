class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"I am a {name}")
class Employee(Person):
    def MyWork(self):
        print("I am an employee")
class Manager(Employee):
    def Myrole(self):
        print("I am a Manager")
    def approove_leave(self):
        print("I can approove Leaves")
obj=Manager("Raj Kumar",23)
obj.MyWork()
obj.Myrole()
obj.approove_leave()

