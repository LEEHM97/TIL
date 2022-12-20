import sys
input = sys.stdin.readline

lst = []
total = 0
for _ in range(5):
    n = int(input())
    total += n
    lst.append(n)

lst.sort()

print(int(total/5))
print(lst[2])    