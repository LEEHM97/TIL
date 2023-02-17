n = int(input())
lst = list(map(int, input().split()))
lst.sort()

target = 1

for i in lst:
    if target < i:
        break
    
    target += i

print(target)