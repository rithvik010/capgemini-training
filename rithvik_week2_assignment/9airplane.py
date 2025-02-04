class Car:
    def move(self):
        print("This is Car, moves on wheels")
class Airplane:
    def move(self):
        print("This is Airplane , Flies through air")
class FlyingCar(Car,Airplane):
    def move(self):
        print("This is FlyingCar moves in both air and land")
        Car.move(self)
        Airplane.move(self)
obj=FlyingCar()
obj.move()
 