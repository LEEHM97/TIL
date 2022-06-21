word = input().upper()

dial = {2:['A','B','C'], 3:['D','E','F'], 4:['G','H','I'], 5:['J','K','L'], 6:['M','N','O'], 
        7:['P','Q','R','S'], 8:['T','U','V'], 9:['W','X','Y','Z']}

word_list = list(word)
sec = len(word_list)

for i in word_list:
    key = [k for k, v in dial.items() if i in v][0]
    sec += key
    
print(sec)