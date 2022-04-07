#!/bin/python3

import os
import math

patternStack = []
dashesStack = []

def createRow(rowNum, welcomeRowNum, numRows, numCols):
    if rowNum == welcomeRowNum:
        welcome = "WELCOME" # 7 chars
        numDashes = (numCols - 7) / 2
        dashes = ""
        for i in range(int(numDashes)):
            dashes += "-"
        row = dashes + welcome + dashes

        return row

    pattern = ".|."

    numPatterns = 0
    
    if rowNum < welcomeRowNum:
        numPatterns = (rowNum * 2) + 1
        patternStack.append(numPatterns)
    else:
        numPatterns = patternStack.pop(len(patternStack) - 1)

    # build patterns
    row = ""
    if(rowNum == 0):
        row = pattern
    else:
        for i in range(numPatterns):
            row += pattern

    # build dashes
    numDashes = 0

    if rowNum < welcomeRowNum:
        numDashes = (numCols - len(row)) / 2
        dashesStack.append(numDashes)
    else:
        numDashes = dashesStack.pop(len(dashesStack) - 1)
    
    dashes = ""
    for i in range(int(numDashes)):
        dashes += "-"
    
    row = dashes + row + dashes

    return row

if __name__ == "__main__":
    dimensions = input().split(' ')
    numRows = int(dimensions[0]) # rows
    numCols = int(dimensions[1]) # cols

    welcomeRowNum = math.floor(numRows / 2) # 0-based index
    
    # create an array of numRows
    doorMat = []
    for i in range(numRows):
        row = createRow(i, welcomeRowNum, numRows, numCols)
        print(row)
