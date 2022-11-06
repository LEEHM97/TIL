import sys
input = sys.stdin.readline

lst = []
max,r,c = 0,0,0

for row in range(9):
    lst.append(list(map(int, input().split())))
    
    for col in range(9):
        if max < lst[row][col]:
            max = lst[row][col]
            r = row
            c = col
print(max)
print(r+1, c+1)