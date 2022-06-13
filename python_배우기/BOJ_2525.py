a, b = map(int, input().split())
c = int(input())

h, m = divmod(c, 60)
if (b + m) // 60 > 0:
    h2, m2 = divmod((b + m), 60)
    print((a + h + h2) % 24, m2)
else:
    print((a + h) % 24, (b + m) % 60 )