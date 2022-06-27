N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
while B:
    tmp = max(B)
    B.remove(tmp)
    tmp2 = min(A)
    A.remove(tmp2)
    cnt += tmp * tmp2
print(cnt)