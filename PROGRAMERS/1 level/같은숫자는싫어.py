from collections import deque

def solution(arr):
    arr = deque(arr)
    answer = []
    while arr:
        num = arr.popleft()
        answer.append(num)
        while True:
            if arr:
                if arr[0] == num:
                    arr.popleft()
                else:
                    break
            else:
                break
    return answer

def solution(arr):
    a = []
    for i in arr:
        print(a[-1:])
        if a[-1:] == [i]: continue
        a.append(i)
    return a

## 인덱싱이 아닌 슬라이싱을 하면 빈 인덱스를 슬라이싱해도 오류가 안남

arr = [1,1,3,3,0,1,1]
print(solution(arr))