def solution(n, m):
    answer = []
    gcd = 0
    lcm = 0
    for i in range(1, max(n, m)+1):
        if n % i == 0 and m % i == 0:
            gcd = max(gcd, i)
    for i in range(max(n, m), (n * m) + 1):
        if i % n == 0 and i % m == 0:
            lcm = i
            break
        
    return [gcd, lcm]

def solution(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        print(c, d)
        print(t)
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

n = 3
m = 12
print(solution(n,m))