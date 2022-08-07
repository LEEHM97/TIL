import sys
input = sys.stdin.readline
cnt = 0

n = int(input())
lst = list(map(int, input().split()))

for i in lst:
    for j in range(2, i):
        if i % j == 0:
            if j == i:
                cnt += 1
            else:
                break
print(cnt)