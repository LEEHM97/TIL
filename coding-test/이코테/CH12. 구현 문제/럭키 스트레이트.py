n = input()

length = len(n)//2
left = 0
right = 0

for i in range(0, length):
    left += int(n[i])

for j in range(length, len(n)):
    right += int(n[j])
    
if left == right:
    print("LUCKY")
else:
    print("READY")