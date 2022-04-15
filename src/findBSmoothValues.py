'''
Find values of x such that x^2 (mod n) is B-smooth
'''
import math
import time
from random import choices, seed

# input: a number n and a factor base of primes chosen by a bound B
# output: a list of candidates such that x^2 is B-smooth and their prime factorizations of x^2
# here we prime factorize a number x^2 and see if its prime factors are less than or equal to B
# or in the factor base given
def findBSmoothValues(n: int, factorBase):
    # print(factorBase)
    start = time.time()
    candidates = []
    squaredFactorizations = []
    factorList = [0 for _ in range(len(factorBase))]

    x = math.ceil(math.sqrt(n))
    # print(x)
    while len(candidates) < len(factorBase) * 2:
        factors = factorize((x*x) % n, factorBase, factorList)
        for i in range(len(factorList)):
            factorList[i] = 0
        if factors[0]:
            # print('Factor', x, time.time() - start)
            print('Solution:', time.time() - start)
            candidates.append(x)
            squaredFactorizations.append(factors[1])
        x += 1

    # print('Time:', time.time() - start)
    return candidates, squaredFactorizations

# input: a number x, a factor base of primes, and a list that represents the factors
# output: the factors of x if it has prime factors in the factorBase
# here we enumerate through the factor base and see if they divide x and how
# they divide x. if the factor base does not fully divide x (x is not equal to 1)
# then x is not B-smooth and we return false with an empty array.
def factorize(x: int, factorBase, factorList):
    for i, prime in enumerate(factorBase):
        if x == 1:
            break
        while x % prime == 0:
            factorList[i] += 1
            x //= prime

    if x != 1:
        return False, []
    factors = [e for e in factorList]
    return True, (factors)

# input: all of the candidates and factorizations, and a count of numbers we want
# output: the selected candidates and factorizations from the input list

def selectCandidates(allCandidates, allSquaredFactorizations, count):
    selection = choices([i for i in range(len(allCandidates))], k=count)
    candidates, squaredFactorizations = [], []
    for i in selection:
        candidates.append(allCandidates[i])
        squaredFactorizations.append(allSquaredFactorizations[i])
    return candidates, squaredFactorizations


# factorBase = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# print(findBSmoothValues(8661028960343, factorBase))
#87463
#2664316859
#8661028960343