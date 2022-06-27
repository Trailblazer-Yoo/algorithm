T = int(input())

# A
cnt_A = 0
while T > 0:
    cnt_A += 1
    T -= 300
if T < 0:
    T += 300
    cnt_A -= 1

# B
cnt_B = 0
while T > 0:
    cnt_B += 1
    T -= 60
if T < 0:
    T += 60
    cnt_B -= 1

# C
cnt_C = 0
while T > 0:
    cnt_C += 1
    T -= 10
if T < 0:
    T += 10
    cnt_C -= 1

if T != 0:
    print(-1)
else:
    print(cnt_A, cnt_B, cnt_C)