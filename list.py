"""
A list is a collection of items that are ordered and mutable
meaning that you can add, remove, or modify elements in the list.
"""
names = ['John', 'Jane', 'Rock']
namesNew = [1, 2, 'John']
names[0] = 'New John'
names.append('my new name')
names.remove('New John')
names.insert(1,'John Doe')
# names.extend(namesNew)
names.sort(reverse=True)
print(names.index('Jane'))