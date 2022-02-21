#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    tallest = 0
    numTallest = 0

    for candle in candles:
        if candle > tallest:
            tallest = candle
            numTallest = 0
        
        if candle == tallest:
            numTallest += 1

    return numTallest

if __name__ == '__main__':
    os.environ["OUTPUT_PATH"] = "output.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
