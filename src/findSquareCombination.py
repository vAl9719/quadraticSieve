import math
import numpy as np
from sympy import *
from factorBaseB import *
from findBSmoothValues import *

'''
Find a combination of x's that multiply to a perfect square
'''



#input: a matrix A
#removes rows that are all 0s to make the later linear algebra a little easier
#from: https://www.geeksforgeeks.org/how-to-remove-array-rows-that-contain-only-0-using-numpy/
def clear_zeros(A):
    # remove rows having all zeroes
    A = A[~np.all(A == 0, axis=1)]




# Alyssa - Use mod 2 linear algebra (Gaussian elimination) on exponents 
# to find products of these x’s that is a square (zero vector)

# Find more smooth values of x^2 - n, find a new linear dependency - how?
# Otherwise, take gcd(a - b, n) to get a nontrivial factor

# input BSmoothList: a 2D array where [x][y] represents the exponent of the yth prime factor of x (b-smooth), this should be mod 2
# output a list of potential candidates for a and b? Or just a and b themselve s.t. there is a linear dependency
#list[x][y] exponent of the yth prime factor of x
#reduce mod 2 then gaussian elimination 
#what to return - a linear combination of these vectors or two candidates? return x and y?
def findSquareCombination(BSmoothList):
    # assume BSmoothList is not transposed
    BSmoothList = BSmoothList.transpose()

    #linear algebra - row reduce using sympy
    BSmoothList_rref = BSmoothList.rref()[0]
    # BSmoothList_rref = clear_zeros(BSmoothList_rref)

    # returns the nullspace and therefore the numbers that may give a dependency
    # will probably want to have a separate array that contains the BSmoothnumbers to correspond to 
    nullspace = BSmoothList_rref.nullspace() 

    rows = len(BSmoothList_rref)
    cols = len(BSmoothList_rref[0])

    return nullspace

    #extract the combination
    #for i in range(len(BSmoothList_rref)):
    #   for j in range(len(BSmoothList_rref)):
            #somehow detect a dependency - multiple 1s in a row?
            #return that row? or trnaslate it to the numbers they correspond to
    #        print("penis")


    #the column dependencies in a row will give which values may give a solution
    #current goal: how to translate rref matrix to the values?


    

