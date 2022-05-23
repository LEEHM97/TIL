n = int(input())
meeting = []
count = 0

for _ in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key = lambda x: (x[1],x[0]))

before_end_time = 0

for i in meeting:
    start, end = i[0], i[1]
    if start >= before_end_time:
        count += 1
        before_end_time = end
print(count)        
