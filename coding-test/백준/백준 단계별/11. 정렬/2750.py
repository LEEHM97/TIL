import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    x = int(input())
    lst.append(x)
    
lst.sort()

for i in lst:
    print(i)