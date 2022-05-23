n = int(input())
t = list(map(int, input().split()))


t.sort()

total_time = t[0]

for i in range(1,len(t)):
    t[i] += t[i-1]
    total_time += t[i]
print(total_time)
