def solution(price, money, count):
    price_all = 0
    for i in range(1, count+1):
        price_all += i * price

    return money - price_all

price = 3
money = 20
count = 4
result = 10
print(solution(price, money, count))