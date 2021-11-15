#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


from math import *
def viralAdvertising(n):
    nb_shared = 5
    liked = 0
    for i in range(n) :
        nb_liked = floor(nb_shared/2)
        nb_shared = nb_liked * 3
        liked += nb_liked
    return liked

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
