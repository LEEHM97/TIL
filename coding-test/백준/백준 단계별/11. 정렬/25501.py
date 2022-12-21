import sys
# input = sys.stdin.readline

def recursion(s, l, r):
    if l >= r: 
        return 1, l
    elif s[l] != s[r]: 
        return 0, l
    else: 
        return recursion(s, l+1, r-1)

T = int(input())

for _ in range(T):
    S = input()
    a, b= recursion(S, 0, len(S)-1)
    print(a, b+1)