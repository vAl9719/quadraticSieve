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

# input M_null: the nullspace of the matrix
# output: vec, the current combination of potential values where a 
# 1 represents which candidates are being used
# and indices, an array of indices of candidates in the nullspace
def setArray(nullspace):
    v = []
    
    #translate nullspace to an array for easier use
    for i in range(0, len(nullspace[0])):
        if nullspace[0][i] != 0:
            v.append(1)
        else:
            v.append(0)
    
    #sum of 1s in the array
    sum = np.sum(v)
    #vec represents the current combination 
    vec = np.zeros(sum, dtype = 'int')
    vec[sum-1] = 1 #here it's just only the last index 
    
    #set up the indices of candidates in the nullspace 
    indices = []
    for i in range(0, len(nullspace[0])):
        if(v[i] == 1):
            indices.append(i)
    
    print(indices)
            
    return [vec, indices]

# input: vec, the current combination vector from the candidates
# output: a new vec, the new combination vector
# if no more combinations can be found, then the program quits
def findCombs(vec):
    index = len(vec) - 1
    while(vec[index] == 1):
        vec[index] = 0
        index = index-1
    
    if(index >= 0):
        vec[index] = 1
    
    else:
        print("No combinations")
        quit()

    return vec    

# input: the RREF matrix, the current combination, and the indices
# output: a full-sized solution vector compute used to calculate x and y
def determineSolVector(M_rref, vec, indices):

    M_rref = np.array(M_rref)
    sol = np.zeros(len(M_rref[0]), dtype= 'int')
    
    for i in range(0, len(vec)):
        if(vec[i] == 1):
            sol[indices[i]] = 1
        else:
            sol[indices[i]] = 2
            
    for i in reversed(range(0, len(M_rref))):
        sum = 0
        for j in range(0, len(M_rref[0])):
            sum = sum + sol[j]*M_rref[i][j]
        zero = (np.argwhere(sol == 0).flatten())
        sum = sum % 2
        if(len(zero) != 0):
            index = zero[len(zero)-1]
            if(sum == 0):
                sol[index] = 2
            else:
                sol[index] = 1
    
    return sol%2    

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

    # calc initial vectors

    vec, indices = setArray(nullspace)
    sol = determineSolVector(BSmoothList_rref, vec, indices)

    return vec, indices, sol, nullspace, BSmoothList_rref

    #solution_nums = [smooth_nums[i] for i in solution_vec]
    #idea is that if nullspace != 0 at index i, then smooth_nums[i] is a potential solution

    #the column dependencies in a row will give which values may give a solution
    #current goal: how to translate rref matrix to the values?
    #or adjust code as needed for specific cases - this feels a bit too straightforward? 


    

