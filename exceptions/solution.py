#!/bin/python3
import os

if __name__ == "__main__":
    numTests = int(input())

    for i in range(numTests):
        test = input()
        a = test.split(' ')[0]
        b = test.split(' ')[1]
        try:
            print(int(a) // int(b))
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)