n, k = map(int, input().split())
count = 0

while(n != 1):
    if n<k:
        count += n+1
        break    
    num =  n - (n//k * k)
    count += num
    k -= num
    
    n = n//k
    count +=1

print(count)
