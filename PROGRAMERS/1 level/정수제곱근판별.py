def solution(n):
    return (int(n ** (1/2)) + 1) ** 2 if n ** (1/2) == int(n ** (1/2)) else -1
n = 3
print(solution(n))