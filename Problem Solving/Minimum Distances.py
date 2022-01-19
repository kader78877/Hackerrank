#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    l_diff = []
    for i,n in enumerate(a) :
        print(i,n)
        a_temp = a[:i]+[None]+a[i+1:]
        if n in a_temp :
            diff = abs(i - a_temp.index(n))
            l_diff.append(diff)
  
    if len(l_diff) == 0 :
        return -1
    elif min(l_diff) == 0:
        return -1
    else :
        return min(l_diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
