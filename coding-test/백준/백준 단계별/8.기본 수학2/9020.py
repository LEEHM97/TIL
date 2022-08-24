import sys
imput = sys.stdin.readline

t = int(input())

def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
    return True
        

for _ in range(t):
    n = int(input())
    a, b = n//2, n//2
    
    while a > 1:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a-=1
            b+=1