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
    vec, indices, sol, nullspace, BSmoothList_rref = findSquareCombination(squaredFactorizations)
    possible = findPossible(candidates, nullspace)

    #initial values
    x = multiplyAll(v, possible)
    xsq = x*x % n
    ysq = factorize(xsq, factorBaseValues)
    y = squareRoot(ysq)

    while inversesModN(x, y, n):
        # x and y are congruent, find a different combination
        vec = findCombs(vec)
        v = determineSolVector(BSmoothList_rref, vec, indices)
        xsq = x*x % n
        ysq = factorize(xsq, factorBase)
        y = squareRoot(ysq)
    
    print("Found x: ", x)
    print("Found y: ", y)

    factor1 = gcd(math.abs(x-y), n)
    factor2 = n/factor1

    print("First factor: ", factor1)
    print("Second factor: ", factor2)

    return factor1, factor2 

# input: v, a vector of 1s and 0s, and a list of nums to multiply
# output: the product
def multiplyAll(v, nums):
    product = 1
    for i in range(0, len(v)):
        if v[i] == 0:
            continue
        product=  product * nums[i]
    
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

def findPossible(candidates, nullspace):
    possible = []
    for i in range(0, len(nullspace[0])):
        if nullspace[0][i] != 0:
            possible.append(candidates[i])

def findAB(candidateList, nullspace): 
    return 0, 0


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
    
