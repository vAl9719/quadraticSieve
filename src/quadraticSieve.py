from tkinter import YView
from factorBaseB import findOptimalB
from findBSmoothValues import findBSmoothValues
from findSquareCombination import findSquareCombination
import util

'''
Main quadratic sieve algorithm
'''


def quadraticSieve(n: int):
    B = findOptimalB(n)
    BSmoothList = findBSmoothValues(n, B)
    while True:
        candidateList = findSquareCombination(BSmoothList)
        a, b = findAB(candidateList)
        if not inversesModN(a, b, n):
            return gcd(a - b, n)


def findAB(candidateList): 
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
    
