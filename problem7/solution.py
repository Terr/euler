#!/usr/bin/python
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

# Keeps track of known primes. We're skipping '2' as we're focussing on odd
# numbers
primes = [3,5,7,11,13]
primes_found = len(primes) + 1 # For the number '2'
x = 15 # Start with this number

while True:
    is_prime = True
    #x_square = x ** 2

    for p in primes:
        if x % p == 0:
            # Number can be divided by another number, so it isn't a prime.
            is_prime = False
            break

    if is_prime:
        primes.append(x)
        primes_found += 1

        if primes_found % 1000 == 0:
            print 'Progress: %d primes found' % primes_found

    if primes_found == 10001:
        # We've found the 10.001st prime
        break

    x += 2 # Skip even numbers

print 'Prime 10.001 is: %d' % primes[-1]
