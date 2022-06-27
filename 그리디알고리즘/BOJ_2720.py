T = int(input())
for _ in range(T):
    m = int(input())

    # 25
    cnt_25 = 0
    while m > 0:
        cnt_25 += 1
        m -= 25
    if m < 0:
        cnt_25 -= 1
        m += 25

    # 10
    cnt_10 = 0
    while m > 0:
        cnt_10 += 1
        m -= 10
    if m < 0:
        cnt_10 -= 1
        m += 10

    # 5
    cnt_5 = 0
    while m > 0:
        cnt_5 += 1
        m -= 5
    if m < 0:
        cnt_5 -= 1
        m += 5
        
    # 1
    cnt_1 = 0
    while m > 0:
        cnt_1 += 1
        m -= 1
    if m < 0:
        cnt_1 -= 1
        m += 1
    print(cnt_25, cnt_10,cnt_5,cnt_1)