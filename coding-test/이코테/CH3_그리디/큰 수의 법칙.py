n,m,k = map(int,input().split())
lst = list(map(int, input().split()))
result = 0
lst.sort()

first = lst[-1]
second = lst[-2]

i, j = divmod(m, (k+1))

result += (k*first+second)*i
result += first * j

print(result)