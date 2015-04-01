__author__ = 'Administrator'

def isPalindrome(n):
    return str(n) == str(n)[::-1]

a = 1000
b = 1000
values = []

for i in range(100, a):
    for j in range(100, b):
        if isPalindrome(i * j):
            values.append(((i*j), i, j))

print max(values)

