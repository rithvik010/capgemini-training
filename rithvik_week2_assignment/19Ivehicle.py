from abc import ABC, abstractmethod
class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(IVehicle):
    def start_engine(self):
        print("Car engine on")
    def stop_engine(self):
        print("Car engine off")
class Bike(IVehicle):
    def start_engine(self):
        print("Bike engine on")
    def stop_engine(self):
        print("Bike engine off")
class Truck(IVehicle):
    def start_engine(self):
        print("Truck engine on")
    def stop_engine(self):
        print("Truck engine off")
car=Car()
car.start_engine()
car.stop_engine()
bike=Bike()
bike.start_engine()
bike.stop_engine()
truck=Truck()
truck.start_engine()
truck.stop_engine()

