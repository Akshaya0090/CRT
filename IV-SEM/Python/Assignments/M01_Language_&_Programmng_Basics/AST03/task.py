str = input()
n1,n2,n3 = list(map(int,input().split()))
avg = n1+n2+n3 // 3
print(str)
if avg >= 35:
    print("pass")
else:
    print("fail")
