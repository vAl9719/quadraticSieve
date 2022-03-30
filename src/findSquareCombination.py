import math
import numpy as np
from sympy import *

'''
Find a combination of x's that multiply to a perfect square
'''

def findSquareCombination():
    pass



# Alyssa - Use mod 2 linear algebra (Gaussian elimination) on exponents to find products of these x’s that is a square (zero vector)
# If a = +-b (mod n), try again
# Find more smooth values of x^2 - n, find a new linear dependency - how?
# Otherwise, take gcd(a - b, n) to get a nontrivial factor


#input: a matrix A
#removes rows that are all 0s to make the later linear algebra a little easier
#from: https://www.geeksforgeeks.org/how-to-remove-array-rows-that-contain-only-0-using-numpy/
def clear_zeros(A):
    # remove rows having all zeroes
    A = A[~np.all(A == 0, axis=1)]
