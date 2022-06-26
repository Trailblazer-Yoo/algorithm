def solution(n):
    s = []
    while True:
        if n == 0:
            break
        qu, re = divmod(n, 3)
        n = qu
        s.append(re)
    
    cnt = 1/3
    answer = 0
    while s:
        tmp = s.pop()
        cnt *= 3
        answer += tmp * cnt
    
    return int(answer)

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        print(tmp)
        n = n // 3
        print(n)

    answer = int(tmp, 3)
    return answer

    
    
n = 45
print(solution(n))
# a, b = divmod(n, 3)
# print(a,b)
# c, d = divmod(a, 3)
# print(c, d)
# e, f = divmod(c, 3)
# print(e, f)
# g, h = divmod(e, 3)
# print(g, h)