N = int(input())

ans = []
check = False
if N % 3 == 0:
    ans.append(N // 3)
    check = True
if N % 5 == 0:
    ans.append(N // 5)
    check = True

for i in range(N//5, 0, -1):
    for j in range(N//3, 0, -1):
        if 5 * i + 3 * j == N:
            ans.append(i + j)
            check = True
            break
        
print(min(ans) if check else -1)


sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)