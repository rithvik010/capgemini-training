class Electronics:
    def __init__(self):
        print("this is electronic device")

class Mobile_phone(Electronics):
    def __init__(self):
        super().__init__()
        self.device_type="mobile phone"
    def use(self):
        print("It is used for communication")
class Smart_phone(Mobile_phone):
   
    def __init__(self):
        super().__init__()
        self.phone_type="smart phone"
    def use(self):
        print("It is used for multi tasking")
        super().use()
    def display(self):
        print(f"Device Type:{self.device_type}\nPhone Type={self.phone_type}")
obj=Smart_phone()
obj.use()
obj.display()