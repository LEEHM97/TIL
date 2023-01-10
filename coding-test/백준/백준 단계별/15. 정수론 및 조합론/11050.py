import sys
input = sys.stdin.readline

n, k = map(int, input().split())
all = 1
div = 1

for i in range(k):
    all *= n-i
    
for j in range(k):
    div *= k-j
    
print(all//div)