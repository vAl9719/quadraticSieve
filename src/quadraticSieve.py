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
    vec, indices, sol, BSmoothList_rref = findSquareCombination(squaredFactorizations)
    print("candidates: ", candidates)

    #initial values
    x = multiplyAll(sol, candidates)
    xsq = x*x % n
    # do we need this actually
    # ysq = factorize(xsq, factorBaseValues) 
    y = squareRoot(x) % n 

    while inversesModN(x, y, n):
        # x and y are congruent, find a different combination
        vec = findCombs(vec)
        sol = determineSolVector(BSmoothList_rref, vec, indices)
        x = multiplyAll(sol, candidates)
        xsq = x*x % n
        #ysq = factorize(xsq, factorBase)
        y = squareRoot(xsq)
    
    print("Found x: ", x)
    print("Found y: ", y)

    factor1 = gcd(x-y, n)
    factor2 = n/factor1

    print("First factor: ", factor1)
    print("Second factor: ", factor2)

    return factor1, factor2 

# input: v, a vector of 1s and 0s, and a list of nums to multiply
# output: the product
def multiplyAll(v, nums):
    product = 1
    for i in range(0, len(nums)):
        if v[i] == 0:
            continue
        product = product * nums[i]
    
    return product

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
        print("x and y are congruent mod n, try again")
        return True 
    return False


def gcd(x, y):
    r = x % y 
    if (r == 0):
        return y
    else:
        return gcd(y, r)
    
quadraticSieve(87463)