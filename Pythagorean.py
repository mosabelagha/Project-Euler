__author__ = 'Administrator'

from math import sqrt

def findPythTriple(c):
    c = c
    for n in range(1, int(sqrt(c))):
        for m in range(1, int(sqrt(c))):
            pythtriple = (abs(n ** 2 - m ** 2), 2*n*m, n**2 + m**2)    # Pythagorean triple, (a,b,c)
            if pythtriple[0] + pythtriple[1] + pythtriple[2] == c:
                return pythtriple


answer = findPythTriple(1000)
print answer
print answer[1] * answer[2] * answer[0]