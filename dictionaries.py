"""
a dictionary is a collection of key-value pairs.
Each key in the dictionary maps to a corresponding value,
and you can use the key to access the value.
Ordered*, changeable, do not allow duplicates
python 3.6 unordered
>= PYthon 3.7 Ordered
"""
fruits = {
    'apple': 1,
    'banana': 2,
    'orange': 3,
    'list': ['list1',2 ,3]
}

users = {
    'username': 'Shayan',
    'Password': 1233456
}
my_dict = {
    "dict1":fruits,
    "dict2":users
}
dict2 = dict(username = 'John', password = 'password' )
my_dict["list"] = True
# my_dict.update({"apple": 5})
# my_dict.update({"ananas": 5})
my_dict["ananas"] = 7
my_dict.pop('ananas')
# my_dict.popitem() from 3.7 removes just the last element
# del my_dict["apple"]
# del my_dict
# my_dict.clear()
my_new_dict = dict(my_dict)
print(my_new_dict['dict1']['apple'])