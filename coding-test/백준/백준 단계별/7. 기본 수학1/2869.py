a, b, v = map(int, input().split())

x = a - b
m = v - a

if x == 1:
    days = v - b
else:
    if m % x == 0:
        days = m // x + 1
    else:
        days = m // x + 2

print(days)