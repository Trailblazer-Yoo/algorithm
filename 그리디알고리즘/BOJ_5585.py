m = 1000 - int(input())

# 500
cnt_500 = 0
while m > 0:
    cnt_500 += 1
    m -= 500
if m < 0:
    cnt_500 -= 1
    m += 500

# 100
cnt_100 = 0
while m > 0:
    cnt_100 += 1
    m -= 100
if m < 0:
    cnt_100 -= 1
    m += 100

# 50
cnt_50 = 0
while m > 0:
    cnt_50 += 1
    m -= 50
if m < 0:
    cnt_50 -= 1
    m += 50
    
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
    
print(cnt_500 + cnt_100 + cnt_50 + cnt_10 + cnt_5 + cnt_1)