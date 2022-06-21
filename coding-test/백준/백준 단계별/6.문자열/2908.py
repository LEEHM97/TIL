a, b = input().split()

a_reverse =  a[::-1]
b_reverse = b[::-1]

print(max(int(a_reverse), int(b_reverse)))