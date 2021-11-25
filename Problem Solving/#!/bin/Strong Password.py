#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    # length 6
    cond_length = True
    n_cond_length = 0
    # at least one digit
    cond_digit = True
    # at least one lowercase
    cond_lowercase = True
    # at least one uppercase
    cond_uppercase = True
    # at least one special character
    cond_special = True
    
    for i in password :
        if i.isupper() and cond_uppercase:
            cond_uppercase = False
        if i.islower() and cond_lowercase:
            cond_lowercase = False
        if i.isdigit() and cond_digit:
            cond_digit = False
        if not(i.isalnum()) and cond_special:
            cond_special = False
    
    if (len(password) + cond_special + cond_digit + cond_lowercase +cond_uppercase >= 6) and (cond_length) :
        cond_length = False
    if len(password) + cond_special + cond_digit + cond_lowercase +cond_uppercase < 6 :
        n_cond_length = 6 - (len(password) + cond_special + cond_digit + cond_lowercase +cond_uppercase)
    
    return cond_special + cond_digit + cond_lowercase +cond_uppercase + n_cond_length
    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
