def solution(n, k):
    tmp = ''
    while n:
        tmp += str(n % k)
        n = n // k
    prime = tmp[::-1]
    answer = prime.split('0')
    count = 0
    for num in answer:
        if num == '1' or num == '':
            continue
        num = int(num)
        count += 1
        for i in range(2,int(int(num)**0.5)+1):
            if int(num)%i==0:
                count -= 1
                break
    return count

n = 437674
k = 3
print(solution(n, k))

## 소수 찾는 방법 : 2부터 자기 자신의 제곱근까지 약수가 없다면 소수