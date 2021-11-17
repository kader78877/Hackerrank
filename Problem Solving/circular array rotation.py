#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # one right rotation
    k_ = k%len(a)
    n = len(a)
    
    # method 3
    # OK
    seq = a[n-k_:] +a[:n-k_]
    
    # method 2 : window (a+a)
    # problem : time exceeding
    """seq_ = a +a 
    seq = seq_[n-k:2*n-k]"""
    
    # method 1 : brute force
    # problem : time exceeding
    """
    for i in range(k_) : 
        seq_bis = seq[-1:] + seq[:-1]
        seq = seq_bis
    """  
        
    return [seq[i] for i in queries]
    
    
    # Write your code here
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
