"""
tuple is an ordered collection of elements similar to a list.
 However, the main difference is that a tuple is an immutable object.
 Once you create a tuple, you cannot modify its contents.
"""

numbers = [4,30,20,80,99,1, 2,2,2,2, 3,100]
#print(type(names))
#names[0] = 'New John'
numbers_tuple = tuple(numbers)
sorted_numbers = sorted(numbers)
# numbers_tuple.index(2)

print(numbers_tuple.count(2))


