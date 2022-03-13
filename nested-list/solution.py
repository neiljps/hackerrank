#!/bin/python3

if __name__ == '__main__':
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        thisScore = [name, score]
        scores.append(thisScore)

    # find the second lowest score
    lowestScore = 101
    lowestScoreList = []

    #print(scores)

    for score in scores:
        if score[1] < lowestScore:
            lowestScore = score[1]
    
    # find names with the lowest score
    for score in scores:
        if score[1] == lowestScore:
            lowestScoreList.append(score[0])

    # remove the names found in lowestScorelist from scores
    for name in lowestScoreList:
        scores.remove([name, lowestScore])
    
    #print(scores)

    # find the next lowest score
    secondLowestScore = 101
    secondLowestScoreList = []
    for score in scores:
        if score[1] < secondLowestScore:
            secondLowestScore = score[1]

    #print(secondLowestScore)
    
    # now that we found the next lowest scores, find the students with the same score
    for score in scores:
        if score[1] == secondLowestScore:
            secondLowestScoreList.append(score[0])

    secondLowestScoreList.sort()

    for score in secondLowestScoreList:
        print(score)
