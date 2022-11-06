import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))
    
for i in range(n):
    b.append(list(map(int, input().split())))

for r in range(n):
    for c in range(m):
        print(a[r][c] + b[r][c], end=' ')
    print()