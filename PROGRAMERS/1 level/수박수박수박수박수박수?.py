def solution(n):
    answer = [0] * n
    qu, re = divmod(n,2)
    for i in range(0, n, 2):
        answer[i] = '수'
    for i in range(1, n, 2):
        answer[i] = '박'
        
    return ''.join(answer)

def solution(n):
    s = "수박" * n
    return s[:n]
    
n = 3
print(solution(n))