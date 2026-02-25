'''li = [1,2,3,4,5]

res = []
for i in li:
    res.append(i**2)
print(res)

ans = [i**2 for i in li ]
print(ans)
#even elements in output
li = [1,2,3,4,5]
res = []
for i in li:
    if i %2 == 0:
        res.append(i**2)
    print(res)

print("*"*5)

li = ['a','b','c']
res = ""
for ch in li:
    res = res + ch+" "
print(res)

print("@" .join (li))'''

'''
#1.pyramid
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
#invert pyramid
n = int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)'''
#diamond
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)




n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+ " ".join([str(j) for j in range (1, i+1)]))
