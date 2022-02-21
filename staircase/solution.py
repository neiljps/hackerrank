#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    staircase = ""

    for i in range(0, n):
        # i is num of spaces
        for j in range(0, n - i - 1):
            staircase += " "

        for j in range(0, i + 1):
            staircase += "#"

        # add newline at end
        staircase += "\n"

    print(staircase)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
