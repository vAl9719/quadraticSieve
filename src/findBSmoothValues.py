'''
Find values of x such that x^2 (mod n) is B-smooth
'''
import math


def findBSmoothValues(n: int, factorBase: list[int]) -> (list[int], list[list[int]]):
    candidates = []
    factorizations = []

    x = math.ceil(math.sqrt(n))
    while len(candidates) < len(factorBase) + 1:
        factors = factorize((x*x) % n, factorBase)
        if factors[0]:
            candidates.append(x)
            factorizations.append(factors[1])
        x += 1

    return candidates, factorizations


def factorize(x: int, factorBase: list[int]) -> (bool, list[int]):
    factors = [0 for _ in range(len(factorBase))]
    for i, prime in enumerate(factorBase):
        if x == 1:
            break
        while x % prime == 0:
            factors[i] += 1
            x //= prime

    if x != 1:
        return False, []
    return True, factors


# testFactorBase = [2, 3, 5]
# testN = 2000
#
# print(findBSmoothValues(391, testFactorBase))
