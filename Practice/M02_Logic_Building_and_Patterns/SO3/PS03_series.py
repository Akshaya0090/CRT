'''arithematic aeries
a = int(input())
d = int(input())
for i in range(10):
    print(a+i*d, end = " ")'''
#geometric series
#1 2
'''
a = int(input())
r = int(input())
for i in range (10):
    print(a * r**i, end = " ")'''
#fibonacci series:
'''
n = int(input())
a = 0
b = 1
for i in range (n):
    print(a, end=" ")
    a,b = b,a+b
#fibonacci using list:
li = [0,1]
for i in range (2,n):
    li.append(li[i-2 ]+ li[i-1])
print(li)'''
# factorial
n = int(input())
if n 