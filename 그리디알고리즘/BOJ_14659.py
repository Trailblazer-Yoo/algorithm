N = int(input())
mont = list(map(int, input().split()))

height = mont[0]
answer = 0
cnt = 0
for i in range(1,N):
    if mont[i] < height:
        cnt += 1
    else:
        height = mont[i]
        answer = max(answer, cnt)
        cnt = 0
answer = max(answer, cnt)
print(answer)