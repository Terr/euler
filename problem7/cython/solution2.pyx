#!/usr/bin/python
# distutils: language = c++
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
cimport cython

from libcpp.vector cimport vector
from libc.math cimport sqrt, floor

import math


# Keeps track of known primes. We're skipping '2' as we're focussing on odd
# numbers
cdef vector[int] primes = map(int, [3,5,7,11,13])

@cython.cdivision(True)
def run():
    global primes

    cdef int primes_found = primes.size() + 1 # For the number '2'
    cdef int x = 15 # Start with this number
    cdef double x_sqrt
    cdef short is_prime

    while True:
        is_prime = 1
        x_sqrt = floor(sqrt(x))

        for p in primes:
            if <double>p > x_sqrt:
                # Checking up to the square root of X is enough. If X is dividible
                # by anything but itself and 1, it should've been caught by now.
                break

            if x % p == 0:
                # Number can be divided by another number, so it isn't a prime.
                is_prime = 0
                break

        if is_prime:
            primes.push_back(x)
            primes_found += 1

            if primes_found % 1000 == 0:
                print 'Progress: %d primes found' % primes_found

        if primes_found == 10001:
            # We've found the 10.001st prime
            break

        x += 2 # Skip even numbers

run()
print 'Prime 10.001 is: %d' % primes.back()
