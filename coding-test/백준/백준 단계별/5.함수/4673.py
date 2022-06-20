def dn(n):
    result = n
    a = n
    while n>9:
        a, b = divmod(n, 10)
        result += b
        n = a
    result += a
    return result

self_num = []
num = list(i for i in range(10001))

for i in range(0, 10001):
    self_num.append(dn(i))

for i in num:
    if i not in self_num:
        print(i)    