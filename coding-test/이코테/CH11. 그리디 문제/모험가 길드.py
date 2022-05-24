from numpy import sort


n = int(input())

array = list(map(int, input().split()))
array = sorted(array)
idx = [0] * (max(array)+1)
count = 0

for i in range(len(array)):
    idx[array[i]] += 1

for i in range(1, len(idx)):
    
    if i > idx[i]:
        break
    g, rest = divmod(idx[i], i)
    count += g
    idx[i+1] + rest
    
print(count)

# solution
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# result = 0 # 총 그룹의 수
# count = 0 # 현재 그룹에 포함된 모험가의 수

# for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
#     count += 1 # 현재 그룹에 해당 모험가를 포함시키기
#     if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
#         result += 1 # 총 그룹의 수 증가시키기
#         count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

# print(result) # 총 그룹의 수 출력