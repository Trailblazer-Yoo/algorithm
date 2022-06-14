N = int(input())
num = 1
count = 0
while N > 0:
    count += 1
    N -= num
    num = (6 * count)
print(count)