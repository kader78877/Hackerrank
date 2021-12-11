#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # 1) create the dict
    arr_set = set(arr)
    dict_val = dict()
    for val in arr_set :
        dict_val[val] = arr.count(val)
        
    # 2) get the max value and max key value
    max_occ = max(dict_val.values())
    for key in dict_val.keys() :
        if dict_val[key] == max_occ :
            max_key = key
            break
    
    # 3) filter and return the sum to delete
    n_to_delete = 0
    for key in dict_val.keys() : 
        if key != max_key :
            n_to_delete+= dict_val[key]
          
    return n_to_delete

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
