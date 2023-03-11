s = input()
result = []
tot = 0

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        tot += int(i)
        
result.sort()

if tot != 0:
    result.append(str(tot))
    
print("".join(result))