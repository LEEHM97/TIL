r = int(input())
result = []
for i in range(r):
    duple = ''
    s = list(map(str, input().split()))
    for j in range(len(s[1])):
        duple = duple + s[1][j] * int(s[0])
    result.append(duple)

for i in result:
    print(i)