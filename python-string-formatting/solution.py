#!/bin/python3

def print_formatted(number):
    # your code goes here
    # get padding size of binary
    binary = str(bin(n))[2:]
    size = len(binary) 

    for i in range(1, n + 1):
        binary = str(bin(i))[2:]

        print(str(i).rjust(size), end=' ')
        print((str(oct(i))[2:].rjust(size)), end=' ')
        print(str(hex(i)[2:].rjust(size).upper()), end=' ')
        print(binary.rjust(size))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

    
