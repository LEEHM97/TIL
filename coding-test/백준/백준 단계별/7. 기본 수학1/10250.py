t = int(input())
room_num = []

for i in range(t):
    h, w, n = map(int, input().split())
    
    q, r = divmod(n, h)
    
    if r == 0:
        floor = h
        num = q
    else:
        floor = r
        num = q+1
    
    
    if num < 10:
        room_num.append(f'{floor}0{num}')
    else:
        room_num.append(f'{floor}{num}')

for i in room_num:
    print(i)