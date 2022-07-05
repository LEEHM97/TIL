x = int(input())

tot = 1
cnt = 1

while(True):
    if x <= tot:
        x_ = tot - x
        b = cnt - x_
        a = 1 + x_
        if cnt % 2 == 0:
            print(f'{b}/{a}')
        else:
            print(f'{a}/{b}')
        break
    cnt += 1
    tot += cnt      