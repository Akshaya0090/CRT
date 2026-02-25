'''#1.pascal Triangle
n = int(input())

for i in range(n+1):
    num = 1
    for j in range (i):
        print(num,end=" ")
        num = num * (i-j)//(j+1)
    print()
'''

# butterfly patterns 
