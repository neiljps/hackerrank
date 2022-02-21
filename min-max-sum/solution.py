#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min = sys.maxsize - 1# 32768 * 2
    max = -sys.maxsize - 1 # 32768 * -2

    # calculate min of 4 of 5 numbers
    for i in range(0, len(arr)):
        # add up min except for i
        thisMin = 0

        subArr = arr.copy()
        subArr.pop(i)

        for num in subArr:
            thisMin += num

        if thisMin < min:
            min = thisMin 
    
        # calculate max of 4 of 5 numbers
    for i in range(0, len(arr)):
        # add up min except for i
        thisMax = 0

        subArr = arr.copy()
        subArr.pop(i)

        for num in subArr:
            thisMax += num

        if thisMax > max:
            max = thisMax 

    print(str(min) + " " + str(max))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
