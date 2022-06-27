from collections import deque

N = int(input())

road = deque(map(int, input().split()))
price = deque(map(int, input().split()))

dp = 0
while road:
    r = road.popleft()
    p = price.popleft()

    while True:
        if not road:
            break
        if p < price[0]:
            r += road.popleft()
            price.popleft()
            continue
        else:
            break

    dp += r*p

print(dp)

# 5
# 1 2 3 2
# 50 30 40 40 20
# 50 + 30 * 7