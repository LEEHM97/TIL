import sys

N, M = map(int, input().split())
currency = [int(input()) for _ in range(N)]
# DP 테이블
d = [10001] * (M+1)
d[0] = 0  # 0원일 경우

for c in range(len(currency)):
    for j in range(currency[c], M+1):
        if d[j - currency[c]] != 10001:
        	# 화폐 단위마다 갱신
            d[j] = min(d[j], d[j - currency[c]] + 1)
 
if d[M] == 10001:
 	print(-1)
else:
	print(d[M])