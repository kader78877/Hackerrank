#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    s_reverse = s[::-1]
    
    s_ascii = [ord(i) for i in s]
    s_reverse_ascii = [ord(i) for i in s_reverse]
    
    s_cost = [abs(s_ascii[i] - s_ascii[i-1]) for i in range(1,len(s))]
    reverse_cost = [abs(s_reverse_ascii[i] - s_reverse_ascii[i-1]) for i in range(1,len(s))]
    
    
    difference_cost = []
    for idx,n in enumerate(s) :
        difference_cost.append(abs(s_ascii[idx] - s_reverse_ascii[idx]))
        
    if s_cost != reverse_cost :
        return 'Not Funny'
    else : 
        return 'Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
