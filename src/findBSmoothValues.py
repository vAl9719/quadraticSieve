'''
Find values of x such that x^2 (mod n) is B-smooth
'''
import math
import time
from random import choices, seed


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


# def findBSmoothValuesFast(n: int, factorBase):
#     start = time.time()
#     candidates = []
#     squaredFactorizations = []
#
#     numThreads = 10
#     sections = [i + 1 for i in range(numThreads)]
#     threads = []
#
#     while len(candidates) < len(factorBase) + 1:
#         for i in range(numThreads):
#             threads.append(Thread(target=findBsmoothSection, args=(n, sections[i], factorBase, candidates, squaredFactorizations)))
#             threads[i].start()
#         for i in range(numThreads):
#             threads[i].join()
#         threads = []
#         for i in range(numThreads):
#             sections[i] += numThreads
#
#     print(time.time() - start)
#     return candidates, squaredFactorizations
#
#
# def findBsmoothSection(n, section, factorBase, candidates, squaredFactorizations):
#     lowerBound, upperBound = math.ceil(math.sqrt(section * n)), math.ceil(math.sqrt((section + 1) * n))
#     xsSquared = [(lowerBound + i) * (lowerBound + i) % n for i in range(upperBound - lowerBound)]
#     factors = [[0 for _ in range(len(factorBase))] for i in range(len(xsSquared))]
#
#     # print('Bounds:', lowerBound, upperBound, section)
#     # print('Squares', xsSquared)
#     # print('Section', section)
#     for pIndex, prime in enumerate(factorBase):
#         residues = solveSquaresModP(n, prime, section)
#         x = math.ceil(lowerBound / prime) * prime
#         # print('Prime:', prime, 'Residues:', residues)
#         while x < upperBound:
#             index = x - lowerBound
#             for offset in residues:
#                 # print('3:', index + offset)
#                 if x + offset >= upperBound:
#                     break
#                 if xsSquared[index + offset] % prime != 0:
#                     # print('uh oh')
#                     return
#                 while xsSquared[index + offset] % prime == 0:
#                     xsSquared[index + offset] //= prime
#                     factors[index + offset][pIndex] += 1
#                     if xsSquared[index + offset] == 1:
#                         candidates.append(x + offset)
#                         squaredFactorizations.append(factors[index + offset])
#             x += prime
#             # print('Squares:', xsSquared, factors)
#     section += 1
#     lowerBound, upperBound = math.ceil(math.sqrt(section * n)), math.ceil(math.sqrt((section + 1) * n))
#     for i in range(upperBound - lowerBound):
#         xsSquared[i] = (lowerBound + i) * (lowerBound + i) % n
#     for i in range(len(xsSquared)):
#         for j in range(len(factorBase)):
#             factors[i][j] = 0
#
#     return candidates, squaredFactorizations



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


# def solveSquaresModP(n, p, section):
#     n = n % p
#     for x in range(p):
#         if (x*x - section * n) % p == 0:
#             if x == 0 or x == p - x:
#                 return (x,)
#             return x, p - x
#     return tuple()


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