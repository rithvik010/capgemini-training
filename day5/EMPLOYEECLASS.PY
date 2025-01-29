class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def set_salary(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

emp = Employee("ali", 50000)
print(f"salary before update:",emp.get_salary())



