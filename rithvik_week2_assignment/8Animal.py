class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Bow!")
class Cat(Animal):
    def speak(self):
        print("Meow!")
obj=Dog()
obj.speak()
obj1=Cat()
obj1.speak()