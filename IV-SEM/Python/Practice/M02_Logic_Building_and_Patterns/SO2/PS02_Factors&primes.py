'''print factors of a given number
n = int(input("enter your number:"))
count = 0

for i in range(1,n//2+1):
    if n %i == 0:
        count += 1
print(count +1)

n = int(input())
count = 0
for i in range(2,n//2):
    if n%i == 0:  
        count +=1
print ("prime" if count == 0 else"not prime")'''


''' print all the prime num in the given range '''
'''start = int(input())
end = int(input())
for n in range(start,end+1):
    counter = 0
    for i in range (2,n//2+1):
        if n%i == 0:
            counter += 1
    if counter == 0:
        print(n,end=" ") 
  '''
'''n = int(input())
fact = 1
for i in range(1,n+1):
    fact =  fact*i
print(fact)'''
# print GCD of 2 num 
#print reverse of a num leecode prob
def reverse (self,x:int) -> int:
    if x<0:
        x = -1 * x
        rev = int(str(x)[: : -1])
        return -1 * rev
    else:
        return int (str(x)[: : -1])
    ''' 9palindrome 43 mul stri  66 plus1'''

