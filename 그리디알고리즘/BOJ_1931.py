import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()
N = int(input())
conf = list(tuple(map(int, input().split())) for _ in range(N))
conf = deque(sorted(conf, key = lambda x: (x[1], x[0])))

cnt = 0
last_num = 0
for i, j in conf:
    if i >= last_num:
        last_num = j
        cnt += 1
print(cnt)

# 시간 기준으로 하면 (3, 5)가 먼저 나옴
# tt = list(range(max(conf,key= lambda x: x[1])[1]))
# conf = sorted(conf, key= lambda x: x[1] - x[0])