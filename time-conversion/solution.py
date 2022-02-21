#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here

    # convert time to military format
    time24h = ""

    # check AM or PM
    if s[-2:].upper() == "AM":
        # don't need to add 12 except for the midnight hour, which will be 00
        if s[:2] == "12":
            time24h = "00" + s[2:-2]
        else:
            time24h = s[:-2] # simply remove AM
    elif s[-2:].upper() == "PM":
        time24h = s[2:-2] # without the hour and without PM

        # it is PM so let's add 12 to the first two numbers
        # if it is not the noon hour
        if (s[:2]) != "12":
            hour = str((int(s[:2]) + 12))
        else:
            hour = s[:2]
        time24h = hour + time24h

    return time24h

if __name__ == '__main__':
    os.environ["OUTPUT_PATH"] = "output.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
