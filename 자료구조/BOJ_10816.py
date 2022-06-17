import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())
list_card = sorted(list(map(int, input().split())))
M = int(input())
for _ in range(M):
    