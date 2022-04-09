#!/bin/python3
import os

if __name__ == "__main__":
    numCountries = int(input())

    s = set()
    for i in range(numCountries):
        country = str(input()).strip()
        s.add(country)
    print(len(s))
