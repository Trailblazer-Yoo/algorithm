import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())
command_list = [input() for _ in range(N)]

q = []
for com in command_list:
    if 'push' in com:
        q.append(int(com.split()[-1]))
    elif com == 'pop':
        print(-1 if len(q) == 0 else q.pop(0))
    elif com == 'size':
        print(len(q))
    elif com == 'empty':
        print(1 if len(q) == 0 else 0)
    elif com == 'front':
        print(-1 if len(q) == 0 else q[0])
    elif com == 'back':
        print(-1 if len(q) == 0 else q[-1])

        