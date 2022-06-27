import sys
input = lambda : sys.stdin.readline()
N = int(input())
ropes = sorted([int(input()) for _ in range(N)], reverse=True)

ans = 0
while ropes:
    min_rope = ropes.pop()
    ans = max(min_rope * (len(ropes) + 1), ans)
print(ans)