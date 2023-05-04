# import Scope as sp
# from Scope import ScopeFunc
import datetime
import platform
import math
'''
In Python, a module is a file containing Python definitions and statements. 
#The file name is the module name with the suffix .py added.
'''

# sp.ScopeFunc()
# print(sp.testDic)
# x = sp.testDic['Year']
# print(x)

# ScopeFunc()

today = datetime.datetime.now()
print(today)
print(today.year)
print(today.month)
print(today.strftime("%a"))
print(today.strftime("%A"))
print(today.strftime("%d"))
print(today.strftime("%b"))
print(today.strftime("%B"))

system = platform.system()
print(system)

print(dir(platform))

# Math Module

a = math.sqrt(64)
b = math.ceil(2.5)
c = math.floor(2.5)
d = math.pi
print(a)
print(b)
print(c)
print(d)

e = min(2,3,5)
f = max(2,3,5)
g = pow(2,4) # 2 * 2 *2 * 2
print(g)

