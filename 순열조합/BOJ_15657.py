n, m = map(int, input().split())
num_list = sorted(list(map(int,input().split())))

s = []
def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return

    for i in range(0, n):
        if len(s) > 0 and s[-1] > num_list[i]:
            continue
        s.append(num_list[i])
        dfs()
        s.pop()

dfs()