import sys

input = lambda: sys.stdin.readline()
N = int(input())

dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N+1):
    if dp[i-1] == i-1:
        dp[i] = 2
    else:
        dp[i] = dp[i-1] + 2
        
print(dp[N]) # 232ms

# 1 2 3 4 5 2 4  2 
# *   *   *   *
# 1 2 3 4 5 6 2 4 6
# *   *   *   *   *
# 1 2 3 4 5 6 7 2 4 6 2 6
# *   *   *   *   *   *


### 시간 초과 코드
# list_card = [i for i in range(1, N+1)]
# while len(list_card) > 2:
#     list_card.pop(0)
#     list_card = list_card[1:] + [list_card[0]]
# print(list_card[-1])

# 투스텝
list_card = [i for i in range(1, N+1)]
while len(list_card) > 1:
    if len(list_card) % 2:
        t = [list_card[-1]]
        t.extend(list_card[1::2])
        list_card = t
    else:
        list_card = list_card[1::2]
        
print(list_card[0]) # 104 ms

from collections import deque
q = deque([i for i in range(1, N+1)])

while len(q) > 1:
    q.popleft()
    q.rotate(-1)
print(q[0]) # 224ms

