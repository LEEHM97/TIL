import sys
from math import sqrt
input = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0:
                return False
        return True

prime_list = [i for i in range(2, 123456*2+1) if isPrime(i)]

while(True):
    n = int(input())
    
    if n == 0:
        break
    else:
        cnt = 0
        for i in prime_list:
            if n < i <= 2*n:
                cnt += 1
    print(cnt)