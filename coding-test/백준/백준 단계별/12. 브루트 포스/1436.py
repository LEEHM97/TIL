import sys
input = sys.stdin.readline

cnt = 0
num_six = 666
n = int(input())

while True:
    if '666' in str(num_six):
        cnt += 1
    if cnt == n:
        print(num_six)
        break
    num_six += 1