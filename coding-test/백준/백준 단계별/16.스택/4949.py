import sys


while True:
    words = input()
    stack = []
    if words == '.':
        break
    
    for i in range(len(words)):
        if words[i] == '[':
            stack.append(words[i])
        elif words[i] == '(':
            stack.append(words[i])
        elif words[i] == ')':
            if len(stack) == 0 or stack[-1] != '(':
                print('no')
                break
            else:
                stack.pop()
        elif words[i] == ']':
            if len(stack) == 0 or stack[-1] != '[':
                print('no')
                break
            else:
                stack.pop()
        elif i==len(words)-1 and words[i] == '.':
            if len(stack) > 0:
                print('no')
            else:
                print('yes')
        else:
            continue