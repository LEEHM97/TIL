## wrong answer, why..?
# croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

# word = input()
# cnt = len(word)

# for i in croatia:
#     if i == 'dz=':
#         cnt -= word.count(i) * 2
#         word = word.replace(i, "")
#     else:
#         cnt -= word.count(i)
# print(cnt)


croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')
print(len(word))