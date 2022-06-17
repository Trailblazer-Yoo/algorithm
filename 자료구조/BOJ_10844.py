import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
n = int(input())
list_command = [input() for _ in range(n)]
q = deque()
for com in list_command:
    if 'push_front' in com:
        c, n = com.split()
        q.appendleft(int(n))
    elif 'push_back' in com:
        c, n = com.split()
        q.append(int(n))
    elif com == 'pop_front':
        try:
            temp = q.popleft()
            print(temp)
        except:
            print(-1)
    elif com == 'pop_back':
        try:
            temp = q.pop()
            print(temp)
        except:
            print(-1)
    elif com == 'size':
        print(len(q))
    elif com == 'empty':
        print(1 if len(q) == 0 else 0)
    elif com == 'front':
        try:
            print(q[0])
        except:
            print(-1)
    elif com == 'back':
        try:
            print(q[-1])
        except:
            print(-1)
        
        