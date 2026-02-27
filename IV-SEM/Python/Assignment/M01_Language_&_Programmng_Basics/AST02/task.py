def even_odd(n):
    if n%2 != 0:
        return("Weird")
    elif n%2 == 0 and n>=2 and n<= 5 :
        return("Not Weird")
    elif n%2 == 0 and n>=5 and n<=20:
        return("Weird")
    elif n%2 == 0 and n>20:
        return("Not Weird")
n = int(input())
print(even_odd(n))
    