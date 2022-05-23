n = int(input())
result = 0

for h in range(0, n+1):
    for m in range(0,60):
        for s in range(0, 60):
            if (str(n) in str(s)) or (str(n) in str(m)) or (str(n) in str(h)):
                result +=1
                
print(result)