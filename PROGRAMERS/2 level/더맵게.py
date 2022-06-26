from collections import deque

def solution(scoville, K):
    answer = 0
    while K > min(scoville):
        print(scoville)
        answer += 1
        scoville = deque(sorted(scoville, reverse=True))
        one = scoville.pop()
        two = scoville.pop()
        scoville.append(one + two * 2)
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))