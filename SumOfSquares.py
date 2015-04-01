__author__ = 'Administrator'


def squaredSum(n):
    return ((n * (n+1)) / 2) ** 2


def sumSquared(n):
    return (n * (n+1) * (2*n+1))/6

k = 100

print squaredSum(k), sumSquared(k), abs(squaredSum(k) - sumSquared(k))