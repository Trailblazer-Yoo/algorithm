T = int(input())

result = 0
for _ in range(T):
    a, b, c = map(int, input().split())

    if a == b and b == c and a == c:
        temp = 10000 + a * 1000
    elif a != b and b != c and a != c:
        temp = max(a, b, c) * 100
    else:
        temp = 1000 + sorted([a,b,c])[1] * 100
    if result < temp:
        result = temp
print(result)