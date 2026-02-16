'''types of errors:
Sysntax errors--> missing colon,
runtime error-->any number divided by 0

debugging techniques:
1)print()
2)try-except
3)using pdp (python debugger)
pdb commands
n
p variable'''


'''try:
    a = int( input("enter a number:"))
    print(10/a)
except ZeroDivisionError:
    print("can not divide by zero")
except ValueError:
    print("invalid input")'''

import pdb
def add(a,b):
    pdp.set_trace()
    return a+b
a = int(input("enter a num:"))
b = int(input("enter another num:"))
print(add(a,b))