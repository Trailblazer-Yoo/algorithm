X = int(input())

num = 0
while X > 0:
    num += 1
    X -= num
X += num

if num % 2 == 0:
    no = X
    deno = num - (X - 1)
else:
    deno = X
    no = num - (X - 1)
print(f'{no}/{deno}')
'''
1 1
2 1
3 2
4 1
5 2
6 3
7 1
'''