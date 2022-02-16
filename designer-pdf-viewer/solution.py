#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    size = 0

    # h is the given size of each letters.
    # h is between 1 and 7

    # word is the given input
    # constraint: word is no more than 10 letters

    # make a dictionary of numbers mapped to characters
    letters = "abcdefghijklmnopqrstuvwxyz"
    lookup = {}
    for i in range(0, len(letters)):
        lookup[letters[i]] = h[i]

    # go through each character in word and add up the size
    tallestSize = 0
    for char in word:
        # look up size of char in the dictionary
        size = lookup[char]
        if size > tallestSize: 
            tallestSize = size
    
    return tallestSize * len(word)



if __name__ == '__main__':
    os.environ["OUTPUT_PATH"] = "output.txt"
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
