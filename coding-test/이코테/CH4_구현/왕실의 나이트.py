loc = input()
row = int(loc[1])
col = int(ord(loc[0]))-int(ord('a'))+1
result = 0

knight = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, 2), (1, -2), (2, -1), (2, 1)]

for i in knight:
    next_row = row+i[0]
    next_col = col+i[1]
    if next_row > 0 and next_col > 0 and next_row<9 and next_col<9 :
        result += 1

print(result)
