#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    aScore = 0
    bScore = 0
    ret = []

    for i in range(0, len(a)):
        if a[i] > b[i]:
            aScore += 1
        elif a[i] < b[i]:
            bScore += 1

    ret.append(aScore)
    ret.append(bScore)
    return ret

if __name__ == '__main__':
    os.environ["OUTPUT_PATH"] = "output.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
