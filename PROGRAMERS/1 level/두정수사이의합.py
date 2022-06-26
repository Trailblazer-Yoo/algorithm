def solution(a, b):
    if b > a:
        return sum([num for num in range(a, b+1)])
    else:
        return sum([num for num in range(b, a+1)])
        

a = 3
b = 5