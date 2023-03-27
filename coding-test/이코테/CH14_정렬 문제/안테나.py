n = int(input())

house = list(map(int, input().split()))

house.sort()

mid = (house[0] + house[-1]) // 2
now = 1e9

for i in house:
    if min(abs(mid - i), now) != now:
        now = abs(mid-i)
        result = i 
        
print(result)