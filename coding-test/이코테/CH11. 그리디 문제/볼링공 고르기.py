import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ball = list(map(int, input().split()))
result = 0

for i in range(len(ball)-1):
    for j in range(i, len(ball)):
        if ball[i] != ball[j]:
            result += 1

print(result)