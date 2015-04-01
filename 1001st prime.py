__author__ = 'Administrator'

from math import sqrt


def checkPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

currNum = 1
index = 10001
counter = 1

while counter != index:
    currNum += 2
    if checkPrime(currNum):
        counter += 1

print currNum