class school:
    def __init__(self):
        self.name="raj"
        self.rollno=123
        
class ug(school):
    def __init__(self):
        super().__init__()
        self.branch="cse"
        self.course="btech"
class pg(ug):
    def __init__(self):
        super().__init__()
        self.subject="computer"
        self.cgpa=9.8
        self.rollno=101
obj=pg()
print(obj.name)
print(obj.course)
print(obj.cgpa)
print(obj.rollno)
    