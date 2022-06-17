import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())
list_integer = sorted(list(map(int, input().split())))
M = int(input())
list_case = list(map(int, input().split()))

for c in list_case:
    start = 0
    end = len(list_integer) - 1
    while start <= end:
        mid = (start + end) // 2
        if list_integer[mid] == c:
            print(1)
            break
        elif list_integer[mid] > c:
            end = mid - 1
        elif list_integer[mid] < c:
            start = mid + 1
    if start > end:
        print(0)