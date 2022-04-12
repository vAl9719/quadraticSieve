from tkinter import YView
from factorBaseB import findOptimalB, factorBase
from findBSmoothValues import findBSmoothValues, factorize
from findSquareCombination import *
import util

'''
Main quadratic sieve algorithm
'''


def quadraticSieve(n: int):
    B = findOptimalB(n)
    factorBaseValues = factorBase(B)
    candidates, squaredFactorizations = findBSmoothValues(n, factorBaseValues)
    nullspace = findSquareCombination(squaredFactorizations)
    print("candidates: ", candidates)
    print("squared factorizations", squaredFactorizations)
    
    index = 0
    comb, sol = retrieveCombination(nullspace, index, candidates)

    #sol = [0, 0, 0, 0, 1]
    # works if sol is correct, so the function somewhere in findSquareComb is wrong
    # how to properly obtain sol from the rref? use nullspace to obtain possibilities? 
    #initial values
    # sol = [0, 1, 0, 0, 1]
    a = multiplyAll(sol, candidates, n)
    b = findB(sol, squaredFactorizations, factorBaseValues, n)

    while inversesModN(a, b, n):
        # x and y are congruent, find a different combination
        index = index + 1
        comb, sol = retrieveCombination(nullspace, index, candidates)
        a = multiplyAll(sol, candidates, n)
        b = findB(sol, squaredFactorizations, factorBaseValues, n)
    
    print("Found a: ", a)
    print("Found b: ", b)

    factor1 = gcd(a-b, n)
    factor2 = n//factor1

    print("First factor: ", factor1)
    print("Second factor: ", factor2)

    return factor1, factor2 

# input: v, a vector of 1s and 0s, and a list of nums to multiply
# output: the product
def multiplyAll(v, nums, n):
    product = 1
    for i in range(0, len(nums)):
        if v[i] == 0:
            continue
        product = (product * nums[i]) % n
    
    return product

def retrieveCombination(nullspace, index, candidates):
    comb = []
    vector = []
    if index >= len(nullspace):
        print("No more combinations")
        quit()
    else:
        for i in range(len(nullspace[0])):
            vector.append(nullspace[index][i])
    
    return comb, vector 

# input: sol (indicator list of candidates used), squaredFactorizations (exponents of
# prime factorization of candidates squared)
# output: corresponding y value
def findB(sol, squaredFactorizations, factorBaseValues, n):
    yFactors = [0 for _ in range(len(factorBaseValues))]
    for i, used in enumerate(sol):
        if used == 1:
            for j, e in enumerate(squaredFactorizations[i]):
                yFactors[j] += squaredFactorizations[i][j]

    y = 1
    for i in range(len(yFactors)):
        y = (y * int(math.pow(factorBaseValues[i], yFactors[i] // 2))) % n
    return y


#input: a number to be square rooted
#output: the square root of a number
# code comes from: https://riptutorial.com/python/example/8751/computing-large-integer-roots
# but the second param is just 2
def squareRoot(num):
    upper_bound = 1
    while upper_bound ** 2 <= num:
        upper_bound *= 2
    
    lower_bound = upper_bound // 2

    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** 2
        if lower_bound < mid and mid_nth < num:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > num:
            upper_bound = mid
        else:
            # Found perfect nth root.
            return mid
    return mid + 1    

def findPossible(candidates, vec):
    possible = []
    for i in range(0, len(vec)):
        if vec[i] != 0:
            possible.append(candidates[i])

    return possible


def inversesModN(x,y, n): # If a = +-b (mod n), try again
    if((x-y)%n == 0 or (x+y)%n == 0):
        print("a and b are congruent mod n, try again")
        return True 
    return False


def gcd(x, y):
    r = x % y 
    if (r == 0):
        return y
    else:
        return gcd(y, r)
    
quadraticSieve(2664316859)
# works for some 12 digits numbers, but not all
#number that didn't work but has factors: 8661028960343 (1121317*7723979)