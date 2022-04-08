import math
import numpy

'''
Find an optimal value of B
'''

def primalityTest(n: int) -> bool:
    # Input a number n, returns True if n is prime and False if n is composite

    return False


def findOptimalB(n: int) -> int:
    # Input a number n, returns the ideal B to use for quadratic sieve

    return math.ceil(math.exp(math.sqrt(math.log(n) * math.log(math.log(n))))**(math.sqrt(2)/4))


def findFactorBase(B: int) -> list[int]:
    # Input integer B, returns all primes up to B

    return [0]


# USE THIS TO TEST
def main():
    print(findOptimalB(10))

if __name__ == "__main__":
    main()
