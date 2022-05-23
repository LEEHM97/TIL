n = int(input())
array = []

for i in range(n):
    score = input().split()
    array.append((score[0], int(score[1])))
    
array = sorted(array, key=lambda num: num[1])

for i in array:
    print(i[0], end= ' ')