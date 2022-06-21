s = list(map(str, input()))
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in alpha:
    if i in s:
        print(f'{s.index(i)}', end=' ')
    else:
        print('-1', end=' ')
        
        
        
# word = input().lower()
# alphabet = list(range(97, 123))

# for x in alphabet:
#     print(word.find(chr(x)), end=' ')