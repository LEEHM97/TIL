import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

hashmap = {}

for i in n_list:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1

for j in m_list:
    if j in hashmap:
        print(hashmap[j], end=" ")
    else:
        print('0', end=" ") 