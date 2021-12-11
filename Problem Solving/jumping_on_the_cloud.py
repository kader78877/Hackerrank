#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    cnt = 0
    current_idx = 0
    while current_idx != len(c)-1 :
        if current_idx + 2 <= len(c)-1 : 
            if (c[current_idx + 2] != 1) :
                current_idx = current_idx + 2 
                cnt += 1
            else :
                current_idx = current_idx + 1
                cnt += 1      
        else:
            current_idx = current_idx + 1
            cnt += 1
    return cnt
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
