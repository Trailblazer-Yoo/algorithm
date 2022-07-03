n, m = map(int, input().split())
num_list = sorted(list(map(int,input().split())))

s = []
visited = [0] * n
result = []
def dfs():
    if len(s) == m:
        result.append(tuple(s[:]))
        return

    for i in range(0, n):
        if visited[i] == 0:
            
            if len(s) > 0 and s[-1] > num_list[i]:
                continue
            visited[i] = 1
            s.append(num_list[i])
            dfs()
            visited[i] = 0
            s.pop()

dfs()
for i in sorted(set(result)):
    print(' '.join(map(str, i)))