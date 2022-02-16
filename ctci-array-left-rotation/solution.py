#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def oneRotation(a):
    # take the first number and put it at the end
    firstNum = a.pop(0)
    a.append(firstNum)
    return a

def rotLeft(a, d):
    # Write your code here
    # numbers always move to the left
    # a = array of numbers to rotate
    # d = number of rotations
    newArr = a.copy()
    for rotations in range(0, d):
        newArr = oneRotation(newArr)
    return newArr


if __name__ == '__main__':
    os.environ["OUTPUT_PATH"] = "output.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()