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
def setArray(matrix):
    v = np.ones(len(matrix[0]), dtype = 'int')
    
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if(matrix[i][j] == 1):
                v[j] = 0
                break
    print("v: ", v)
    #sum of 1s in the array
    sum = np.sum(v)
    #vec represents the current combination 
    vec = np.zeros(sum, dtype = 'int')
    vec[sum-1] = 1 #here it's just only the last index 
    
    #set up the indices of candidates in the nullspace 
    indices = np.zeros(sum, dtype='int')

    # print(len(matrix[0]))
    k = 0
    for i in range(0, len(matrix[0])):
        if(v[i] == 1):
            indices[k] = i
            k = k+1
    
    # print("indices is, ", indices)
            
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
    print("matrix is, ", BSmoothList)
    # assume matrix is not mod 2, mod 2 all elements 
    for i in range (0,len(BSmoothList)): 
        for j in range (0, len(BSmoothList[0])):
            BSmoothList[i][j] = BSmoothList[i][j] % 2
    
    print("mod 2 matrix is, ", BSmoothList)
    # assume BSmoothList is not transposed
    M = Matrix(BSmoothList)
    M = M.transpose()


    #linear algebra - row reduce using sympy
    
    BSmoothList_rref = np.array(M.rref()[0])%2

    print("rref is, ", BSmoothList_rref)

    #BSmoothList_rref = clear_zeros(BSmoothList_rref)

    # returns the nullspace and therefore the numbers that may give a dependency
    # each nonzero value corresponds to a number in the BSmooth numbers list
    #nullspace = BSmoothList_rref.nullspace() 
    #print("nullspace is, ", nullspace)

    #for i in range (0,len(nullspace)): 
    #    nullspace[i] = nullspace[i]%2

    # calc initial vectors

    vec, indices = setArray(BSmoothList_rref)
    sol = determineSolVector(BSmoothList_rref, vec, indices)
    vec = findCombs(vec)
    sol = determineSolVector(BSmoothList_rref, vec, indices)
    vec = findCombs(vec)
    sol = determineSolVector(BSmoothList_rref, vec, indices)
    print("vec", vec)
    print("sol", sol)

    return vec, indices, sol, BSmoothList_rref

    #solution_nums = [smooth_nums[i] for i in solution_vec]
    #idea is that if nullspace != 0 at index i, then smooth_nums[i] is a potential solution

    #the column dependencies in a row will give which values may give a solution
    #current goal: how to translate rref matrix to the values?
    #or adjust code as needed for specific cases - this feels a bit too straightforward? 


    

