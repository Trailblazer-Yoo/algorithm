import sys

input = lambda: sys.stdin.readline().strip()

T = int(input())
case = [input() for _ in range(T)]

for PS in case:
    stack = []

    for s in PS:
        stack.append(s)
        try:
            if stack[-2] + stack[-1] == '()':
                stack.pop()
                stack.pop()
        except:
            pass
    if len(stack) > 0:
        print("NO")
    else:
        print("YES")

# import sys

# input = lambda: sys.stdin.readline().strip()

# T = int(input())
# case = [input() for _ in range(T)]

# for PS in case:
#     count = 0
#     while True:
#         temp = PS.replace('()','')
#         if PS == temp:
#             break
#         else:
#             count += 1
#             PS = temp
    
#     print('YES' if len(PS) == 0 else 'NO')