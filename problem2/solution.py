#!/usr/bin/python
"""Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""

def fib(a, b):
    return a+b

total = 0
terms = [0, 1]

while True:
    t1, t2 = terms
    t3 = fib(t1, t2)

    if t3 > 4000000:
        break

    terms = [t2, t3]

    if t3 % 2 == 0:
        total += t3

print 'Result: %d' % total
