# from abc import ABC,abstractmethod
# class Father(ABC):
#     @abstractmethod
#     def displ(self):
#        # print("hello son")
#         pass
#     def show(self):
#         print("concretemethod")
# class Son(Father):
#     def displ(self):
#         print("son is implementing the abstract method")
# class Daughter(Father):
#     def displ(self):
#         print("daughter is implementing abstract class")
# obj=Son()
# obj.displ()
# obj.show()
# obj2=Daughter()
# obj2.displ()
# obj2.show()

#creating interface
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Bark!"
obj3=Dog()
obj3.make_sound()