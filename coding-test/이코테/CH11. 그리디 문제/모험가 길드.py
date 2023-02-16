n = int(input())

lst = list(map(int, input().split()))
lst.sort()

cnt = 0
result = 0

for i in lst:
    cnt += 1
    
    if i <= cnt:
        result += 1
        cnt = 0

print(result)