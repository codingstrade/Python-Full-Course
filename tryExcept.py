"""
In Python, the try-except statement is used to catch and handle exceptions
that might occur during the execution of a program.
The try block contains the code that might raise an exception,
and the except block handles the exception if one occurs.
"""

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another Number: "))
    result = x / y
    print("The Result is ", result)
except ZeroDivisionError:
    print("Error: You cannot divide by Zero. ")
except NameError:
    print('No variable with this name exists')
else:
    print('Everything is as it should be')
finally:
    print('The finally is running!')

name = 'coding'

if not type(name) is int:
    raise TypeError("The type should be integer!")