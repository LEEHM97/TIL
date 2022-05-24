from posixpath import split


n, m = map(int, input().split())
result = 0

for i in range(n):
    array = list(map(int, input().split()))
    n_min = min(array)
    result = max(result, n_min)
    
print(result)