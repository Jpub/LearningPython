#!python
from __future__ import print_function                      # File factorials.py
from functools import reduce
from timeit import repeat
import math

def fact0(N):                                              # Recursive
    if N == 1:                                             # Fails at 999 by default
        return N
    else:
        return N * fact0(N-1)

def fact1(N):
    return N if N == 1 else N * fact1(N-1)                 # Recursive, one-liner

def fact2(N):                                              # Functional
    return reduce(lambda x, y: x * y, range(1, N+1))

def fact3(N):
    res = 1
    for i in range(1, N+1): res *= i                       # Iterative
    return res

def fact4(N):
    return math.factorial(N)                               # Stdlib "batteries"

# Tests
print(fact0(6), fact1(6), fact2(6), fact3(6), fact4(6))    # 6*5*4*3*2*1: all 720
print(fact0(500) == fact1(500) == fact2(500) == fact3(500) == fact4(500))  # True

for test in (fact0, fact1, fact2, fact3, fact4):
    print(test.__name__, min(repeat(stmt=lambda: test(500), number=20, repeat=3)))

r"""
C:\code> py -3 factorials.py
720 720 720 720 720
True
fact0 0.003990868798355564
fact1 0.003901433457907475
fact2 0.002732909419593966
fact3 0.002052614370939676
fact4 0.0003401475243271501
"""
