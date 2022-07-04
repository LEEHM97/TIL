n = int(input())

room_num = 1
tot = 1

while(True):
    if tot >= n:
        break
    
    tot += 6 * room_num
    room_num += 1
    
print(room_num)