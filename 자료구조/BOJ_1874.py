import sys

input = lambda : sys.stdin.readline()

n = int(input())

case = []
result = []
count = 1
for _ in range(n):
    num = int(input())
    while count <= num: ## not in 이 시간이 많이 걸림 while 조건문 사용
        for i in range(count, num + 1):
            case.append(i)
            result.append('+')
        count = num + 1
    last_n = case.pop()
    if last_n != num:
        result.append('NO')
        break
    else:
        result.append('-')
if result[-1] != 'NO':
    for i in result:
        print(i)
else:
    print('NO')


    
# a = ['+', '+', '+', '+', '-', '-', '+', '+', '-', '+', '+', '-', '-', '-', '-', '-']

# case = []
# count = 0
# for i in a:
#     if i == '+':
#         count += 1
#         case.append(count)
#     elif i == '-':
#         case.pop()
#     print(case)