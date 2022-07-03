import sys

input = lambda : sys.stdin.readline()

n = int(input())
k = int(input())
list_card = [int(input()) for i in range(n)]

visited = [0] * n
num = ''
array = set() # 중복 제거

# 재귀 구현
def com(cnt): # cnt + 1 형태로
    global num
    if cnt == k: # k만큼 돌았으면 빠져나오게
        array.add(num)
        return
    
    for i in range(n):
        if visited[i] == 0: # 아직 방문하지 않았다면
            visited[i] = 1 # 해당 방문처리
            tmp = str(list_card[i]) # 해당 인덱스의 문자열 가져오기
            num += tmp
            
            com(cnt+1) # 재귀적으로 들어가서 다음 문자열을 가져옴
            
            visited[i] = 0 # 마지막 문자열을 제거하고 방문했던 처리를 원상태로 돌려놓음
            num = num[:-len(tmp)] # 마지막 문자열을 제거하기 위해 [:-len]으로 마지막 문자열 제외하고 슬라이싱

com(0)
print(len(array))
        
'''
1단계 : stack 안에 k개 만큼의 숫자를 넣는다.
2단계 : stack 안의 k개의 숫자로 만들 수 있는 모든 경우의 수를 만들어 set 안에 넣는다
3단계 : stack 안의 마지막 숫자를 빼고 그 다음 숫자를 넣는다.
'''