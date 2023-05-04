'''
In Python, scope refers to the area of a program where a variable can be accessed.
The scope of a variable is determined by where it is defined in the code.
There are two main types of scope in Python: global scope and local scope.
'''
name = 'Python' #global scope
def ScopeFunc():
    name = 'Testing coding' # local scope
    def testScope():
            print(name)
    testScope()

testDic = {
    'name':'Tesla',
    'Year': 2023
}

print(name)
ScopeFunc()
print(name)