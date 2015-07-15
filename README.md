import random
l = []
for i in range(0, 30):
    l.append(random.randint(0, 99))
even = 0
odd = 0
for i in range(0, 30):
    if l[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print even
print odd
largest = 0
smallest = 99
for i in range(0, 30):
    if  l[i] > largest:
        largest = l[i]
    if l[i] < smallest:
        smallest = l[i]
print l
print largest
print smallest
