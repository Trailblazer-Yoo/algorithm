def solution(price, money, count):
    price_all = 0
    for i in range(1, count+1):
        price_all += i * price

    return price_all - money if money < price_all else 0

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

price = 3
money = 20
count = 4
result = 10
print(solution(price, money, count))