import sys
input = sys.stdin.readline

x_lst = []
y_lst = []

for _ in range(3):
    a, b = map(int, input().split())
    x_lst.append(a)
    y_lst.append(b)
    
for i in x_lst:
    if x_lst.count(i) == 1:
        x = i

for j in y_lst:
    if y_lst.count(j) == 1:
        y = j
        
print(x, y)