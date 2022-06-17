import sys

input = lambda: sys.stdin.readline()

K = int(input())
s = []
for _ in range(K):
    i = int(input())
    if i == 0:
        s.pop()
    else:
        s.append(i)
print(0 if len(s)==0 else sum(s))