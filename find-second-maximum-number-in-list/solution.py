#!/bin/python3

import sys

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    nums = list(arr)

    maxNum = -100 #sys.maxsize * -1
    secondMaxNum = -100 #sys.maxsize * -1

    # find max num
    for num in nums:
        if num > maxNum:
            maxNum = num

    # remove max num
    nums.remove(maxNum) 

    for num in nums:
        if num > secondMaxNum and num != maxNum:
            secondMaxNum = num

    print(secondMaxNum)
        