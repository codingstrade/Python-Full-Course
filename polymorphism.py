"""
Polymorphism is a fundamental concept in object-oriented
programming that refers to the ability of objects of different
types to be used interchangeably.
"""

my_string = 'coding'
print(len(my_string))
myTuple = ('Tesla','Bmw','Mercedes')
print(len(myTuple))
mydi = {
    'name':'Tesla',
    'year': 2023
}
print(len(mydi))

class Animal:
    def make_sound(self):
        print('The Animal make a sound')

class Dog(Animal):
    def make_sound(self):
        print('The Dog barks')
class Cat(Animal):
    def make_sound(self):
        print('The Cat meows')

my_animals = [Dog(),Cat(),Animal()]

for animals in my_animals:
    animals.make_sound()
