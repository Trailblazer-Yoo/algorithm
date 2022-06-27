import heapq

def solution(scoville, k):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
        
    answer = 0
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except:
            return -1
        answer +=1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))