s = input()

zeros = 0
ones = 0

if s[0] == '0':
    zeros += 1
elif s[0] == '1':
    ones += 1
    
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            zeros += 1
        elif s[i+1] == '1':
            ones += 1
print(min(zeros, ones))