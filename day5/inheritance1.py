class parent:
    def __init__(self):
        self.bigNose="7cm"

    def display_parent(self):
        print("this isnpqrent class")
class child(parent):
    def display_child(self):
        print("this is child class")

obj=child()
obj.display_parent()
obj.display_child()        
print(obj.bigNose)
