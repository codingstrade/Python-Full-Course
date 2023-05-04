'''
In Python, a class is a blueprint for creating objects
that share similar attributes and behaviors,
while an object is a specific, concrete instance of a class with
its own set of values for the attributes defined in the class.
'''

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def myfunction(self):
        print('Hello from my own Function' + self.name)

class cars:
    pass

person1 = Person('Shayan',100)
person2 = Person('John Doe',200)
person1.age = 10
# del person1.age
# del person1
print(person1.name)
print(person1.age)
print(person1)
print(person2)
print(person1.myfunction())
print(cars)
