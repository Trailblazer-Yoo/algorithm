def solution(d, budget):
    d = sorted(d, reverse=True)

    answer = 0
    while d:

        budget -= d.pop()
        if budget < 0:
            break
        answer += 1
    return answer

d = [1,3,2,5,4]
budget = 9

print(solution(d, budget))


def solution(d, budget):
    d.sort()
    print(d)
    while budget < sum(d):
        d.pop()
    return len(d)