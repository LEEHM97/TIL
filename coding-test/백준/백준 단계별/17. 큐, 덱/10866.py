import sys
from collections import deque

input = sys.stdin.readline
queue = deque([])
n = int(input())

for _ in range(n):
    words = input().split()
    word = words[0]
    
    if word == 'push_front':
        queue.appendleft(words[1])
        
    elif word == 'push_back':
        queue.append(words[1])
        
    elif word == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
            
    elif word == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
            
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