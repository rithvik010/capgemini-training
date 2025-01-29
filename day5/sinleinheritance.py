class parent:
    def display(self):
        print("this is parent class")

class Child(parent):
    def display_child(self):
        print("this is child class ")
obj=Child()
obj.display()
obj.display_child()
