import sys
input = sys.stdin.readline

n = int(input())

A_list = list(map(int, input().split()))
A_list.sort()

print(A_list[0]*A_list[-1])