from tkinter import YView
from factorBaseB import findOptimalB, factorBase
from findBSmoothValues import findBSmoothValues, factorize
from findSquareCombination import *
import time

'''
Main quadratic sieve algorithm
'''

# input: a large number n that is the product of 2 large primes
# output: its factors (ideally!)
def quadraticSieve(n: int):
    startTime = time.time()
    B = 2 * findOptimalB(n)

    factorBaseValues = factorBase(B)
    print('Factor base: ', factorBaseValues)
    allCandidates, allSquaredFactorizations = findBSmoothValues(n, factorBaseValues)

    while True:
        candidates, squaredFactorizations = selectCandidates(allCandidates, allSquaredFactorizations,
                                                             len(factorBaseValues) + 1)
        print('Candidates:', candidates)
        nullspace = findSquareCombination(squaredFactorizations)

        for index in range(len(nullspace)):
            comb, sol = retrieveCombination(nullspace, index, candidates)
            a = multiplyAll(sol, candidates, n)
            b = findB(sol, squaredFactorizations, factorBaseValues, n)
            if not inversesModN(a, b, n):
                print("a and b:", a, b)

                factor1 = gcd(a - b, n)
                factor2 = n // factor1

                print("Factors:", factor1, factor2)
                endTime = time.time()
                print("Runtime: ", endTime - startTime)
                return factor1, factor2
                # a and b are congruent, find a different combination

# input: v, a vector of 1s and 0s, and a list of nums to multiply (1 is include, 0 is don't include)
# based off the nullspace
# output: the product of the nums that correspond with the 1s
def multiplyAll(v, nums, n):
    product = 1
    for i in range(0, len(nums)):
        if v[i] == 0:
            continue
        product = (product * nums[i]) % n
    
    return product

# input: the nullspace of the matrix, the index in the nullspace, the candidate B-smooth numbers
# output: a combination of candidate numbers, a specific column of the nullspace based on the index
def retrieveCombination(nullspace, index, candidates):
    comb = []
    vector = []
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


# input: a number to be square rooted
# output: the square root of a number
# code comes from: https://riptutorial.com/python/example/8751/computing-large-integer-roots
# but the second parameter is just 2
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

# input: x and y, the numbers we want to check congruence, and n, the modulo we wre in
# output: if x and y (or -y) are congruent mod n
def inversesModN(x,y, n): # If a = +-b (mod n), try again
    if((x-y)%n == 0 or (x+y)%n == 0):
        print("a and b are congruent mod n, try again")
        return True 
    return False

# input: two numbers, x and y 
# output: the greatest common divisor of x and y 
# using Euclidean algorithm
def gcd(x, y):
    r = x % y 
    if (r == 0):
        return y
    else:
        return gcd(y, r)
    
print(quadraticSieve(8661028960343))

#2664316859

#87463
#2664316859
#8661028960343
#16921456439215439701