import sys
input = sys.stdin.readline

N = int(input())
result = 0

for i in range(1, N+1):
    lst = list(map(int, str(i)))
    result = i + sum(lst)
    
    if result == N:
        print(i)
        break
    
    if i == N:
        print(0)
        