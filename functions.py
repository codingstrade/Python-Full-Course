"""
In programming, a function is a block of code that performs
a specific task or set of tasks.
It is designed to be reusable and can be called from other
parts of the code to perform the same task without having to write
the same code repeatedly.
"""

def greet(name, lname):
    print("Hello and welcome to my coding channel " + name + lname + ' ')


def addmynumbers(num1, num2):
    return num1 + num2

result = addmynumbers(1000,7)
print(result)

# Arbitrary Arguments, *args
# in cases if you don't know how many parameters you need

def cars(*carname):
    print('the car '+ carname[0] + ' is the best! ')

cars('Tesla', 'Bmw')

# keyword argument

def carsTwo(carname, model):
    print('the car with model ' + model + ' from' + carname + ' is the best!' )

carsTwo(model="x1", carname="Bmw")

# Arbitrary Keyword Arguments, **kwargs
def carsThree(**cars):
    print("the last model of "+ cars['carname'] + ' is worst')

carsThree(engine='something', carname='Tesla')

# default value

def language(selectedLanguage = 'english'):
    print('your using the language ' + selectedLanguage)

language()

def languages(language):
    for x in language:
        print(x)
listLanguages = ['English', 'German', 'Hindi', 'Chinees']

languages(listLanguages)

