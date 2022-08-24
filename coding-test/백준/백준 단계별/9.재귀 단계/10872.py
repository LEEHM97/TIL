import sys
input = sys.stdin.readline

def fibo(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fibo(n-1)

n = int(input())
print(fibo(n))