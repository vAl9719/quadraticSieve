import math
import numpy
import random
import sys

'''
Find an optimal value of B
'''

def isPrime(n: int, k: int) -> bool:
    # Input a number n > 0 and iterations k, return False if n is composite and True
    # if n is probably prime. The higher the k, the more accurate this test become
    # Base cases
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True

    # Check if n is even
    elif n % 2 == 0:
        return False

    # n is odd, so find odd m such that n-1 = (2^c)*m
    # Use m to run Miller-Rabin Primality Test k times
    # If any of k trials is composite, then return False.
    m = n - 1
    c = 0
    while m % 2 == 0:
        m //= 2
        c += 1

    for _ in range(k):
        if millerRabin(n, m, c) == False:
            return False
    return True


def millerRabin(n: int, m: int, c: int) -> bool:
    # Implementation of the Miller-Rabin Primality Test (used in isPrime)
    a = random.randint(2, n - 2)
    b = (a ** m) % n

    if (b == 1) or (b == n - 1):
        return True

    # This loop computes b_1 to b_(c-1)
    for _ in range(c - 1):
        b = (b ** 2) % n

        if b == 1:
            return False
        elif b == n - 1:
            return True

    return False


def findOptimalB(n: int) -> int:
    # Input a number n, returns the ideal B to use for quadratic sieve
    return math.ceil(math.exp(math.sqrt(math.log(n) * math.log(math.log(n))))**(math.sqrt(2)/4))


def factorBase(B: int) -> list:
    # Input integer B, returns all primes up to B

    factorbase = []

    for i in range(2, B + 1):
        if (isPrime(i, 15)):
            factorbase.append(i)

    return factorbase


# # USE THIS TO TEST
# def main():
#     # print(isPrime(int(sys.argv[1]), 10))
#     print(factorBase(int(sys.argv[1])))
#
# if __name__ == "__main__":
#     main()
