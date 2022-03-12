#!/bin/python3

if __name__ == '__main__':
    N = int(input())

    ret = []
    
    # N is number of commands
    for i in range(0, N):
        command = input().split(' ')

        if command[0] == "append":
            ret.append(int(command[1]))
        elif command[0] == "print":
            print(ret)
        elif command[0] == "insert":
            ret.insert(int(command[1]), int(command[2]))
        elif command[0] == "remove":
            ret.remove(int(command[1]))
        elif command[0] == "sort":
            ret.sort()
        elif command[0] == "pop":
            ret.pop()
        elif command[0] == "reverse":
            ret.reverse()

