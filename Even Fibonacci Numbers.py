from math import sqrt

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1) + F(n-2)
def Fmath(n):
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

sum =0

i = 0
while Fmath(i) < 4000000:
    if(Fmath(i)&1 == 0):
        sum += Fmath(i)
    i += 1

print(sum)
