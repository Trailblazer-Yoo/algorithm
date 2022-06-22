def solution(a, b):

    return sum([x * y for x, y in zip(a, b)])

solution = lambda x, y: sum(a*b for a, b in zip(x, y))

a = [1,2,3,4]
b = [-3,-1,0,2]
print(solution(a, b))