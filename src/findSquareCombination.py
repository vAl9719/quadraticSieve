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


# input BSmoothList: a 2D array where [x][y] represents the exponent of the yth prime factor of x (b-smooth)
# output nullspace: the nullspace of BSmoothList, AKA a subsequence of b smooth numbers that has a product square
# gaussian elimination can be a bottleneck but is often not a problem since the matrix is sparce
# however there are faster implementations, but here we use sympy to row reduce and find the null space of a matrix
# faster implementation can be implemented referencing (papers)

def findSquareCombination(BSmoothList):

    # assume BSmoothList is not transposed
    M = Matrix(BSmoothList)
    M = M.transpose()

    # assume matrix is not mod 2, mod 2 all elements 
    for i in range (0,len(M)): 
        for j in range (0, len(M[0])):
            M[i][j] = M[i][j] % 2

    #linear algebra - row reduce using sympy
    BSmoothList_rref = M.rref()[0]
    # BSmoothList_rref = clear_zeros(BSmoothList_rref)

    print(BSmoothList_rref)

    # returns the nullspace and therefore the numbers that may give a dependency
    # each nonzero value corresponds to a number in the BSmooth numbers list
    nullspace = BSmoothList_rref.nullspace() 
    print(nullspace)

    for i in range (0,len(nullspace)): 
        nullspace[i] = nullspace[i]%2

    rows = len(BSmoothList_rref)
    cols = len(BSmoothList_rref[0])

    return nullspace

    #solution_nums = [smooth_nums[i] for i in solution_vec]
    #idea is that if nullspace != 0 at index i, then smooth_nums[i] is a potential solution

    #the column dependencies in a row will give which values may give a solution
    #current goal: how to translate rref matrix to the values?
    #or adjust code as needed for specific cases - this feels a bit too straightforward? 


    

