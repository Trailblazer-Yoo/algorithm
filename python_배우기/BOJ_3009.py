import sys

input = lambda : sys.stdin.readline().strip()

temp_x = []
temp_y = []
for _ in range(3):
    x, y = map(int, input().split())
    temp_x.append(x)
    temp_y.append(y)
temp_xset = set(temp_x)
temp_yset = set(temp_y)

for x in temp_xset:
    if temp_x.count(x) == 1:
        print(x, end=' ')
for y in temp_yset:
    if temp_y.count(y) == 1:
        print(y)