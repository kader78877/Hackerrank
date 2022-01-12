#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#
def isKaprekar(n) :
    n_square = n**2
    n_square_str = str(n_square)
    if len(n_square_str) %2 != 0 :
        n_square_str = '0' + n_square_str
    
    n_middle = int(len(n_square_str)/2)
    l = int(n_square_str[:n_middle])
    r = int(n_square_str[n_middle:])
        
    if l+r == n:
        return True
    else :
        return False

def kaprekarNumbers(p, q):
    kapreparlist = [str(i) for i in range(p,q+1) if isKaprekar(i) ]
    if kapreparlist != [] :
        print(' '.join(kapreparlist))
    else :
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
