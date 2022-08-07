import sys

input = sys.stdin.readline

m = int(input())
n = int(input())
lst = []

for i in range(m, n+1):
    for j in range(2, i+1):
        if i % j == 0:
            if j == i:
                lst.append(i)
            else:
                break
if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])