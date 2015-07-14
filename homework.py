__author__ = 'armen'
import random
import re
l = []
for i in range(0, 199):
    l.append(random.randint(0, 99))
c = raw_input('Input the number: ')
if (re.match('[+-]*\d+', c)):
    c = int(c)
    if ((c < 0) or (c > 99)):
        print('Wrong input (out of range [0..99]).')
    else:
        a = 0
        for i in range(0, 199):
            if l[i] == c:
                a += 1
                print "- found an occurrence at index", i
        if a > 0:
            print "Found occurrences:", a
        else:
            print("No occurrences found.")
else:
    print("Wrong input (invalid format).")
