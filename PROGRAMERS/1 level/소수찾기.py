def solution(n):
    a = [False, False] + [True] * (n-1)
    primes = []
    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
n = 10
print(solution(n))