import sys

input = lambda : sys.stdin.readline()

m, n = map(int,input().split())
list_num = sorted(list(map(int, input().split())))

visited = [0] * m

s = []
# 재귀 구현
def com(cnt): # cnt + 1 형태로
    if cnt == n: # k만큼 돌았으면 빠져나오게
        print(' '.join(map(str, s)))
        return
    
    for i in range(m):
        if visited[i] == 0: # 아직 방문하지 않았다면
            visited[i] = 1 # 해당 방문처리
            s.append(list_num[i])
            
            com(cnt+1) # 재귀적으로 들어가서 다음 문자열을 가져옴
            
            visited[i] = 0 # 마지막 문자열을 제거하고 방문했던 처리를 원상태로 돌려놓음
            s.pop() # 마지막 문자열을 제거하기 위해 [:-len]으로 마지막 문자열 제외하고 슬라이싱

com(0)


s = []
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if list_num[i] not in s:
            s.append(list_num[i])
            dfs()
            s.pop()
dfs()