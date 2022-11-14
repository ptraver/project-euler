# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:30:37 2019

@author: 33743

"""

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from euler27 import isprime
from math import sqrt, floor

large_num = 600851475143

#Identifies all the factors of large_num
factors = [a for a in range(1, floor(sqrt(large_num))) if large_num % a == 0]

print(max(a for a in factors if isprime(a)))
