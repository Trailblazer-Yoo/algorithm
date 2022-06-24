def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        tmp = 0
        for n in range(1, num + 1):
            if num % n == 0: 
                tmp += 1
        if tmp % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer

left = 13
right = 17
print(solution(left, right))


# 제곱수는 약수의 갯수가 홀수
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer