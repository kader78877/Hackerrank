#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    
    # init variables
    n_prob = sum(arr)
    i_chapter = 1
    i_prob = 1
    i_page = 1
    n_special = 0
    page = []
    k_prob = i_prob + k
    while n_prob != 0 :

        if i_prob + k - 1 < arr[i_chapter-1] :
            k_prob = i_prob + k
        if i_prob + k - 1 >= arr[i_chapter-1] : 
            k_prob = arr[i_chapter-1] + 1
        prob_to_add = [i for i in range(i_prob,k_prob)]

        if i_page in prob_to_add :
            n_special +=1
        
        if arr[i_chapter-1] not in prob_to_add :
            i_prob = k_prob
        if arr[i_chapter-1] in prob_to_add :
            n_prob = n_prob - arr[i_chapter-1]
            i_chapter += 1
            i_prob = 1
            k_prob = i_prob + k
        page.append(prob_to_add)
        i_page += 1
    return n_special
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
