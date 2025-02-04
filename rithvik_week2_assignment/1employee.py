class Employee:
    def __init__(self,name,id,role,phone_no):
        self.name=name
        self.id=id
        self.role=role
        self.phone_no=phone_no
    def display(self):
        print(f"NAME :{self.name}")
        print(f"ID :{self.id}")
        print(f"ROLE :{self.role}")
        print(f"PHONE NUMBER :{self.phone_no}")
employee1=Employee("Raj Kumar",12012,"Analyst",9900000000)
employee1.display()
