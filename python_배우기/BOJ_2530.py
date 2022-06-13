a,b,c = map(int, input().split())
d = int(input())

m,s = divmod(d, 60)
b += m
c += s

m, c = divmod(c, 60)
b += m

h, b = divmod(b, 60)
a += h
    
print(a % 24, b, c)