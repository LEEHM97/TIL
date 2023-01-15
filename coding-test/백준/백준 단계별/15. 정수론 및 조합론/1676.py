import sys
import math
input = sys.stdin.readline

n = int(input())
fact = math.factorial(n)
cnt = 0

while True:
    if (fact % 10) != 0:
        break
    fact //= 10
    cnt += 1
    
print(cnt)
