#!/bin/python
"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

#number_range = range(1, 11)
number_range = range(1, 101)

sum_of_squares = sum([x**2 for x in number_range])
square_of_sum = sum(number_range) ** 2

print 'Sum of squares: %d' % sum_of_squares
print 'Square of the sum: %d' % square_of_sum
print 'Difference: %d' % (square_of_sum - sum_of_squares)
