n, k = map(int, input().split())
# 동전 리스트
a = []
# 필요한 동전 개수
count = 0

# n개 만큼 동전 삽입
for _ in range(n):
    a.append(int(input()))

while k!=0:
    for i in reversed(range(len(a))):
        count += k // a[i]
        k %= a[i]

print(count)