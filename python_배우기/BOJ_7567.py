dish = list(input())

result = 0
temp = [0]
n = len(dish)
for _ in range(n):
    d = dish.pop(0)
    if temp[-1] == d:
        result += 5
    else:
        result += 10
    temp.append(d)
print(result)
        