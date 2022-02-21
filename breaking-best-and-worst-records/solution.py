#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    # game 1 is the baseline game
    mostPts = 0
    lastMostPts = scores[0]
    leastPts = 0
    lastLeastPts = scores[0]

    for score in scores[1:]:
        if score > lastMostPts:
            mostPts += 1
            lastMostPts = score
        elif score < lastLeastPts:
            leastPts += 1
            lastLeastPts = score

    ret = [mostPts, leastPts]
    return ret

if __name__ == '__main__':
    os.environ["OUTPUT_PATH"] = "output.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
