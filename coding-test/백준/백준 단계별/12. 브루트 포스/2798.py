import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))
tmp = 0

for x in range(N):
    for y in range(x+1, N):
        for z in range(y+1, N):
            if lst[x]+lst[y]+lst[z] == M:
                tmp = lst[x]+lst[y]+lst[z]
                break
            elif lst[x]+lst[y]+lst[z] < M:
                tmp = max(tmp, lst[x]+lst[y]+lst[z])
            
print(tmp)