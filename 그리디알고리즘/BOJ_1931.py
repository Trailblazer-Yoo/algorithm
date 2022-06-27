import sys

input = lambda : sys.stdin.readline().strip()
N = int(input())
conf = [tuple(map(int, input().split())) for _ in range(N)]
# tt = list(range(max(conf,key= lambda x: x[1])[1]))
# conf = sorted(conf, key= lambda x: x[1] - x[0])
conf = sorted(conf, key=lambda x : (x[0], [1]))
print(conf)
