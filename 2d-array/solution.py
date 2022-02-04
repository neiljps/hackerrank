#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    maxSum = float('-inf')
    MAX_LENGTH = 6 # this problem's inputs are exactly 6 lines of 6 space-separated integers
    for i in range(0, MAX_LENGTH - 2):
        for j in range(0, MAX_LENGTH - 2):
            # if within range
            if (i < (MAX_LENGTH)) and (j < (MAX_LENGTH)):
                sum = 0
                # sum up the top 3 numbers
                sum += arr[i][j] + arr[i][j + 1] + arr[i][j + 2]

                # next the middle number
                sum += arr[i + 1][j + 1]

                # then the bottom 3 numbers
                sum += arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]

                if sum > maxSum:
                    maxSum = sum
    return maxSum

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = "output.txt" # added this line
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

