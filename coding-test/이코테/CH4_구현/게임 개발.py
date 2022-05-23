n, m = map(int, input().split())
x, y, direct = map(int, input().split())
total_map = []
result = 1
turn_time = 0

for i in range(n):
    total_map.append(list(map(int, input().split())))
    
total_map[x][y] = 1
now = total_map[x][y]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direct
    direct -= 1
    if direct == -1:
        direct = 3

while True:
    turn_left()
    nx = x+dx[direct]
    ny = y+dy[direct]
    
    if total_map[nx][ny] == 0:
        total_map[nx][ny] = 1
        x = nx
        y = ny
        result += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x-dx[direct]
        ny = y-dx[direct]
        
        if total_map[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
        
print(result)




