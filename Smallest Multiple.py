__author__ = 'Administrator'


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


n = 20
currentLCM = 1

for i in range(1,n+1):
    currentLCM = lcm(currentLCM, i)
    print currentLCM

