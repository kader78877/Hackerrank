#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    
    s = [sorted(list(i)) for i in arr]
    all_element = []
    for i in s : 
        all_element += i
    all_element = set(all_element) 
    gem_value = 0
    for element in all_element :
        element_value  = True
        for i in arr :
            if element not in i :
                element_value = False
        if element_value :
            gem_value += 1    
    return gem_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
