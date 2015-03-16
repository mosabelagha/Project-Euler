n = 999
three = int(n/3) + 1
five = int(n/5) + 1
fivethree = int(n/(3*5)) + 1

sum = 0

print(three, five, fivethree)
for i in range(1, three):
    sum += 3*i
print(sum)
for i in range(1, five):
    sum += 5*i
print(sum)

for i in range(1, fivethree):
    sum -= 15*i
print(sum)

print(sum)
