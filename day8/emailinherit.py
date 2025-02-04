from abc import ABC,abstractmethod
class Email(ABC):
    def displ(self):
        pass
class Sms(Email):
    def displ(self):
        print("sms")
class Whatsaap(Email):
    def displ(self):              
        print("Whatsaap")
      