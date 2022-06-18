while True:
    sentence = input()
    if sentence == '.':
        break
    
    q = []
    temp = True
    for word in sentence:
        if word == '(' or word == '[':
           q.append(word)
        elif word == ')':
            if not q or q[-1] == '[':
                temp = False
                break
            elif q[-1] == '(':
                q.pop()
        elif word == ']':
            if not q or q[-1] == '(':
                temp = False
                break
            elif q[-1] == '[':
                q.pop()
    if temp == True and not q:
        print('yes')
    else:
        print('no')