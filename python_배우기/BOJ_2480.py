a, b, c = map(int, input().split())

if a == b and b == c and a == c:
    print(10000 + a * 1000)
elif a != b and b != c and a != c:
    print(max(a, b, c) * 100)
else:
    print(1000 + sorted([a,b,c])[1] * 100)