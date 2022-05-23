n = int(input())
array = list(map(int, input().split()))

array.sort()
left = 0
right = n-1

_sum = 2e+9
result = []

while left < right:
    s = array[left] + array[right]
    if abs(s) < _sum:
        _sum = abs(s)
        result = [array[left], array[right]]
    if s > 0:
        right -= 1
    else:
        left += 1
        
        
print(result[0], result[1])
