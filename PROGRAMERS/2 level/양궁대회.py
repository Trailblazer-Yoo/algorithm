# lion = []
# def makeCase(n):
#     if n == 0:
#         return
#     tmp = [0] * 11
    
    
    
#     pass


# def solution(n, info):
#     info = info[::-1]
#     cases = []


        
#     answer = []
#     return answer

# n = 5
# info = [2,1,1,1,0,0,0,0,0,0,0]

n = 3
# [3,0,0], [0,3,0], [0,0,3], [2,1,0], [2,0,1], [1,2,0], [0,2,1], [1,0,2], [0,1,2], [1,1,1]

case = []
def makeCase(n, st):

    if n == 0:
        case.append(list(st))
        return
    
    for i in range(1, n + 1):
        
        st += str(i)
        k = n - i
        print(st)
        print(k, n)
        makeCase(k,st)
        
makeCase(4, '')
print(case)
        
## 1단계 : n = 3일때, 모든 숫자를 이용해 합이 3이 되는 숫자들의 조합 구하기
## 2단계 : 각 조합들이 length = 11인 

