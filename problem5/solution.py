#!/usr/bin/python
"""2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

#dividers = range(1, 11)
dividers = range(1, 21)
x = 2
res_found = False

while True:
    for d in dividers:
        if x % d == 0:
            res_found = True
        else:
            res_found = False
            break

    if res_found:
        break

    x += 1

print 'Result: %d' % x
