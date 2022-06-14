V = int(input())
vote = input()

result = 0
for v in vote:
    if v == 'A':
        result += 1
    elif v == 'B':
        result -= 1
        
if result > 0:
    print('A')
elif result < 0:
    print('B')
else:
    print('Tie')