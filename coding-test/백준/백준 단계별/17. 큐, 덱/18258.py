import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque([])

for _ in range(n):
    words = input().split()
    word = words[0]
    
    if word == 'push':
        queue.append(words[1])
    elif word == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif word == 'size':
        print(len(queue))
    elif word == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif word == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif word == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])