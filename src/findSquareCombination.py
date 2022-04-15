import math
import numpy as np
from sympy import *
from factorBaseB import *
from findBSmoothValues import *

'''
Find a combination of x's that multiply to a perfect square
'''   

# input BSmoothList: a 2D array where [x][y] represents the exponent of the yth prime factor of x (b-smooth)
# output nullspace: the nullspace of BSmoothList, AKA a subsequence of b smooth numbers that has a product square
# gaussian elimination can be a bottleneck but is often not a problem since the matrix is sparce
# however there are faster implementations, but here we use sympy to row reduce and find the null space of a matrix
# faster implementation can be implemented referencing (papers)

def findSquareCombination(BSmoothListOriginal):
    BSmoothList = [[x for x in col] for col in BSmoothListOriginal]

    # print("matrix is, ", BSmoothList)
    # assume matrix is not mod 2, mod 2 all elements 
    for i in range (0,len(BSmoothList)):
        for j in range (0, len(BSmoothList[0])):
            BSmoothList[i][j] = BSmoothList[i][j] % 2
    
    # print("mod 2 matrix is, ", BSmoothList)

    # assume BSmoothList is not transposed
    M = Matrix(BSmoothList)
    M = M.transpose()


    #linear algebra - row reduce using sympy
    
    M = M.rref()[0]

    print("rref is, ", M)

    # returns the nullspace and therefore the numbers that may give a dependency
    # each nonzero value corresponds to a number in the BSmooth numbers list
    nullspace = M.nullspace() 

    for i in range (0,len(nullspace)): 
        for j in range(0, len(nullspace[0])):
            nullspace[i][j] = nullspace[i][j]%2

    nullspace = np.array(nullspace)
    # print("nullspace is, ", nullspace)

    #for i in range(0, len(nullspace[0])):
    #    print("element in nullspace, ", nullspace[0][i]) # from nullspace, try and grab the right combination
    # traverse through nullspace, maybe try and grab combinations and see if they work?

    # calc initial vectors

    #vec, indices = setArray(BSmoothList_rref)
    #sol = determineSolVector(BSmoothList_rref, vec, indices)
    #print("vec, ", vec)
    #print("sol, ", sol)
    return nullspace

    #solution_nums = [smooth_nums[i] for i in solution_vec]
    #idea is that if nullspace != 0 at index i, then smooth_nums[i] is a potential solution

    #the column dependencies in a row will give which values may give a solution
    #current goal: how to translate rref matrix to the values?
    #or adjust code as needed for specific cases - this feels a bit too straightforward? 


    

