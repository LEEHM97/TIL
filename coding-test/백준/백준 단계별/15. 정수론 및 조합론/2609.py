import sys
input = sys.stdin.readline

a, b = map(int, input().split())
gcd = 1
i = 1

while True:
    i += 1
    if i > min(a, b):
        break
    
    if a % i == 0 and b % i == 0:
        a //= i
        b //= i
        gcd *= i
        i = 1

print(gcd)
print(gcd*a*b)