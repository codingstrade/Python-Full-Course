'''
In Python, a lambda function is a small anonymous function
that can take any number of arguments, but can only have one expression.
'''

multiply = lambda x, y: x * y

print(multiply(2,14))

def square(n):
    return lambda x : x ** n

square_of_2 = square(3)

print(square_of_2(3))

reverse = lambda x: x[::-1]
print(reverse("hello"))

my_list = [1,2,3,4,5,-6,7,8,9,29]

max_val = lambda x:min(x)
print(max_val(my_list))

