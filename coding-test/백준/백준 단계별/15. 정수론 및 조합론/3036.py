import sys
import math

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

for i in range(1, len(lst)):
    lcm = math.lcm(lst[0], lst[i])
    print(str(lcm // lst[i]) + "/" + str(lcm // lst[0]))