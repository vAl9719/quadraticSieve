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
# uses functions from the sympy package to do matrix operations
def findSquareCombination(BSmoothListOriginal):
    BSmoothList = [[x for x in col] for col in BSmoothListOriginal]

    # assume matrix is not mod 2, mod 2 all elements 
    for i in range (0,len(BSmoothList)):
        for j in range (0, len(BSmoothList[0])):
            BSmoothList[i][j] = BSmoothList[i][j] % 2

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

    return nullspace 


    

