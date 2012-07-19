#!/usr/bin/python
"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#prime = 13195
prime = 600851475143

file_prime = open('prime_numbers.txt', 'r')
prime_numbers = map(int, [x.strip() for x in file_prime.read().split(',')])

factorials = []
remaining = prime
while True:
    for x in prime_numbers:
        if remaining % x == 0:
            factorials.append(x)
            remaining = remaining / x
            break

    if remaining <= 2:
        break

print 'Factorials: %s' % ', '.join(map(str, factorials))
