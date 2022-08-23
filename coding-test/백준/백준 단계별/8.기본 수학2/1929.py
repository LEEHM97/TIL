import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0:
                return False
        return True

for i in range(n, m+1):
    if isPrime(i):
        print(i)