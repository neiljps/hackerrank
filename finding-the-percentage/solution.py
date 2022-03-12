#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # find the scores for this name
    scores = student_marks[query_name]

    total = float(0)
    numScores = 0
    for score in scores:
        total += score
        numScores += 1
    
    avg = float(total / numScores)
    print(format(avg, '.2f'))

