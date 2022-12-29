import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

result = abs(w-x)

if abs(h-y) < result:
    result = abs(h-y)
    
if x < result:
    result = x

if y < result:
    result = y

print(result) 