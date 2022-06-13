# 15분 50초
import sys

input = lambda: sys.stdin.readline()

S = int(input())
num = 1
result = 0
while True:
    S -= num
    result += 1
    if S < 0:
        S += num
        S += (num - 1)
        result -= 2
    elif S == 0:
        break
    else:
        num += 1
print(result)

# 11
# 1 10
# 2 8
# 3 5
# 4 1
# 5 -4
# 5 5
