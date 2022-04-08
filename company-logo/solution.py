#!/bin/python3
import os

def sortFunc(i):
    #print("i: " + str(i))
    #return i
    #return str(i.split(' ')[0]) + str(i.split[' '][1])
    return i

if __name__ == "__main__":
    dict = {}

    s = input()
    
    for char in s:
        # check if char is in dict
        if char in dict:
            instances = dict[char] 
            dict[char] = int(instances) + 1
        else: # if not, add char into dict
            dict[char] = 1

    #print(dict)

    maxCount = 0
    # get highest count
    for char in dict:
        if int(dict[char]) > maxCount:
            maxCount = int(dict[char])
    
    everything = []
    for cnt in range(maxCount, 0, -1):
        # sort output by occurence count
        sortedList = []

        # loop through dict looking for this cnt
        for char in dict:
            if int(dict[char]) == cnt:
                sortedList.append(char)
                # sortedList.append(str(dict[char]) + ' ' + char)
        
        sortedList.sort(key=sortFunc)

        toEverything = []
        for char in sortedList:
            toEverything.append(char + " " + str(cnt))
            #print(char + " " + str(cnt))
        
        everything.append(toEverything)

    #print(everything)

    # get the top 3 from everything
    cnt = 0
    for alist in everything:
        if cnt == 3: break
        for item in alist:
            if(cnt == 3): break
            print(item)
            cnt += 1
            
        
