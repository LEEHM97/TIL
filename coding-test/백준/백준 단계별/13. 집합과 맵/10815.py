import sys
input = sys.stdin.readline

N = int(input())
N_lst = set(map(str, input().split()))

M = int(input())
M_lst = list(map(str, input().split()))

for i in M_lst:
    if i in N_lst:
        print(1, end=" ")
    else:
        print(0, end=" ")