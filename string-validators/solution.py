#!/bin/python3

if __name__ == '__main__':
    s = input()

    # alphanumeric
    hasAnyAlphaNum = False
    for char in s:
        if char.isalnum():
            hasAnyAlphaNum = True
            break
    print(hasAnyAlphaNum)

    # true if has any alpha
    hasAlpha = False
    for char in s:
        if char.isalpha():
            hasAlpha = True
            break
    print(hasAlpha)
    
    # true if has any digits
    hasDigits = False
    for char in s:
        if char.isdigit():
            hasDigits = True
            break
    print(hasDigits)

    # true if has any lowercase
    hasLower = False
    for char in s:
        if char.islower():
            hasLower = True
            break
    print(hasLower)

    # true if has any uppercase
    hasUpper = False
    for char in s:
        if char.isupper():
            hasUpper = True
            break

    print(hasUpper)
