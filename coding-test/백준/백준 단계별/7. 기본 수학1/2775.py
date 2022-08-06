t = int(input())
result = []

for _ in range(t):
    k = int(input())
    n = int(input())
    
    people = [i for i in range(1, n+1)]
    
    for _ in range(k):
        for i in range(1, n):
            people[i] += people[i-1]
    result.append(people[-1])
    
for i in result:
    print(i)