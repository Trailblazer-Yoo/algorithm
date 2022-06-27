def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            tmp = [yellow // i + 2, i + 2]
        if sum(tmp) * 2 - 4 == brown:
            return tmp

brown = 24
yellow = 24
print(solution(brown, yellow))