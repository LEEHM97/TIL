import sys
import numpy as np
input = sys.stdin.readline

n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    num1, num2, num3 = map(int, input().split())
    a.append([num1, num2, num3])
    
for i in range(n):
    num1, num2, num3 = map(int, input().split())
    b.append([num1, num2, num3])

a = np.array(a)
b = np.array(b)

for i in range(a):
    c = a[i] + b[i]
    