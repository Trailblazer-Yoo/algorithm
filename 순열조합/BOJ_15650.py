n, m = map(int, input().split())
list_num = list(range(1, n+1))

s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)


# BOJ_5568 처럼 풀이하는 법
num = ''
visited = [0] * n
result = set()
def select(cnt):
    global num
    if cnt == m:
        result.add(num)
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            tmp = str(list_num[i])
            if len(num) > 0 and int(num[-1]) > int(tmp):
                visited[i] = 0
                continue
            num += tmp
            
            select(cnt + 1)
            
            visited[i] = 0
            num = num[:-len(tmp)]

select(0)
for row in sorted(result):
    print(*row)