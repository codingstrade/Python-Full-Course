"""
In Python, an iterator is an object that implements the
iterator protocol, which consists of two methods:
__iter__() and __next__().
The __iter__() method returns the iterator object itself,
and the __next__() method returns the next item from the iterator.

An iterator represents a sequence of values that can be
accessed one at a time. Each time the __next__() method is called
on an iterator, it returns the next value in the sequence,
and raises a StopIteration exception when there are no more values.
"""

my_list = [1,2,3,4,'string',5,6,7]
my_string = 'Shayan'
my_iter = iter(my_string)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
for x in my_string:
    print(x)

