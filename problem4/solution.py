#!/usr/bin/python
# -*- coding: utf-8 -*-
"""A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import copy

#num_range = range(99, 9, -1)
num_range = range(999, 99, -1)

def reverse_string(str):
    new_str = ''
    str_len = len(str)

    for x in range(str_len -1, -1, -1):
        new_str += str[x]

    return new_str

rangex = copy.copy(num_range)
rangey = copy.copy(num_range)
max_multiplication = 0

for x in rangex:
    for y in rangey:
        result = x * y

        str_res = str(result)
        res_len = len(str_res)
        if res_len % 2 == 0:
            # Split number in equal parts and check for palindrome
            h1 = str_res[:res_len/2]
            h2 = str_res[res_len/2:]

            if h1 == reverse_string(h2):
                max_multiplication = max(result, max_multiplication)

print 'Largest palindrome: %d' % max_multiplication

