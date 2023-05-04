"""
In Python, inheritance is a mechanism that allows a new class
to be based on an existing class. The new class,
known as the derived class or subclass, inherits attributes and behaviors
from the existing class, known as the base class or superclass.
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary,bonus):
        # Employee.__init__(self,name,salary)
        super().__init__(name,salary)
        self.bonus = bonus

    def get_salary(self):
        return self.salary + self.bonus

varClass = Manager("John", 3000,2000)
print(varClass.name)

manager1 = Manager('Alice',50000,10000)
print(manager1.get_salary())