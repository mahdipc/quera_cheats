import numpy as np
from sympy import *

N=int(input())
def PraimNumber(number):
    res=nt.isprime(np.array([1,3,5,7,9])+number*10)
