"""
the if...else statement allows you to execute different code blocks
based on a condition.
The basic syntax of an if...else statement is:

if condition:
    # Code to execute if condition is true
else:
    # Code to execute if condition is false
"""
x = -1

if x > 0:
    print('x is positive')
elif x < 0:
    print('x is negative')
else:
    print('x is Zero')

# Short Statement / Ternary Operators
print('x is Positive') if x < 0 else print('x is negative')

# Keyword And, Or, Not Operator
z = 5
y = 0
i = 10
if not i < z:
    print('the condition is true')
else:
    print('nothing left')

# nested if
a = 1
b = 0

if a > 0:
    if b > 0:
        pass
    else:
        print('a is positive but x is not')
else:
    print('a is zero or negative')