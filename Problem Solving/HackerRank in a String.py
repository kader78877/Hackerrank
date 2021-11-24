#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    goal = 'hackerrank'
    index_goal = 0
    for i,k in enumerate(s) :
        if goal[index_goal] == k :
            index_goal += 1
        if index_goal == len(goal) :
            break
    if index_goal == len(goal) :
        return 'YES'
    else :
        return 'NO'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
