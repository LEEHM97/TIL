import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

start = 0
end = len(lst)
mid = (lst[0] + lst[-1]) // 2

while True:
    result = 0
        
    for i in range(len(lst)-1, 0, -1):
        result += lst[i] - mid
        if result > m:
            mid += 1
            break
    if result == m:
        print(mid)
        break
    elif result < m:
        mid -= 1
