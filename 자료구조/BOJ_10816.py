import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())
list_card = sorted(list(map(int, input().split())))
M = int(input())
case = list(map(int, input().split()))

result = []
for num in case:
    start = 0
    end = len(list_card) - 1
    while True:
        mid = int(start + end // 2)
        print(mid)
        if list_card[mid] < num:
            start = mid
        elif list_card[mid] > num:
            end = mid
        elif list_card[mid] == num:
            break
    result.append(list_card[start:end].count(num))
    