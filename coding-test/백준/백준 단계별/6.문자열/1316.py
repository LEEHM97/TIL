n = int(input())
cnt = 0

for i in range(n):
    word = input()
    word_list = list(dict.fromkeys(list(word)))
    
    for i in word_list:   
        word = word.lstrip(i)
    if len(word) == 0:
        cnt += 1


print(cnt)