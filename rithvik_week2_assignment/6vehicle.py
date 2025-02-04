class Vehicle:
    def transport(self):
        pass
class Car(Vehicle):
    def fuel(self):
        print("Diesel or Petrol")
class Bike(Vehicle):
    def fuel(self):
        print("Petrol")
class Electric_Car(Car):
    def fuel(self):
        print("Electric Charge")
        super().fuel()  #using super key to acces fuel from class car
obj=Car()
obj.fuel()
obj2=Bike()
obj2.fuel()
obj3=Electric_Car()
obj3.fuel()
