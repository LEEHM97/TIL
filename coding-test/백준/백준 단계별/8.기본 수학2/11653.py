import sys
input = sys.stdin.readline

n = int(input())
root_n = n**(1/2)
pivot = 2

while(n > 1):
    if n % pivot == 0:
        print(pivot)
        n //= pivot
    elif pivot > root_n:
        print(n)
        break
    else:
        pivot += 1
