import sys

s = input()
result = int(s[0])


for i in range(1, len(s)):
    if int(s[i]) < 2 or result < 2:
        result += int(s[i])
    else:
        result *= int(s[i])
        
        if result > 2000000000:
            result /= int(s[i])
            result += int(s[i])
            
print(result)