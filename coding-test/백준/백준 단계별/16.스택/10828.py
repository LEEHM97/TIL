import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().split()
    word = command[0]
    
    if word == "push":
        stack.append(command[1])
    elif word == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    elif word == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif word == "size":
        print(len(stack))
    else:
        if len(stack) > 0:
            print(0)
        else:
            print(1)
        