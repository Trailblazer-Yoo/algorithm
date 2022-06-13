import sys

input = lambda: sys.stdin.readline()
result = 0
for _ in range(5):
    s = int(input())
    if s >= 40:
        result += s
    else:
        result += 40
print(int(result/5))
        