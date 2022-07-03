n, m = map(int, input().split())
num_list = sorted(list(map(int,input().split())))

s = []
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return

    for i in range(start, n):
        if len(s) > 0 and s[-1] > num_list[i]:
            continue
        else:
            s.append(num_list[i])
            dfs(i+1)
            s.pop()

dfs(0)