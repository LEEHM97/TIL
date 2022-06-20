n = int(input())
n_str = input()

strToInt = list(map(int, n_str))

sum = 0

for i in strToInt:
    sum += i
print(sum)