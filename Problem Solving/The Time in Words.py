#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    def past_hour(h,m) :
        pass
    def to_hour(h,m) :
        pass
    
    if m %15 == 0 :
        if m==30 :
            return 'half past ' + d[h]
        if m==0 :
            return d[h] + " o' clock"
        if m==15 :
            return 'quarter past ' + d[h]
        if m==45 : 
            return 'quarter to ' + d[h+1]
    elif m >30 :
        diff = 60-m
        diff_deci = (diff//10)*10
        if diff not in d.keys() :
            diff_unit = diff%10
            diff_str = d[diff_deci] + ' ' + d[diff_unit]
        else :
            diff_str = d[diff]
        return diff_str + ' minutes to ' + d[h+1]
    elif m < 30 :
        m_deci = 10*(m//10)
        if m%10 == 0 :
            return d[m_deci] + ' minutes past ' + d[h]
        else :
            m_unit = m%10
            if m_deci == 0 :
                if m_unit > 1:
                    return d[m_unit] + ' minutes past ' + d[h]
                else :
                    return d[m_unit] + ' minute past ' + d[h]
            else :
                return d[m_deci] +' ' + d[m_unit] + ' minutes past ' + d[h]


            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
