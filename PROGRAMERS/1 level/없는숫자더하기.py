def solution(numbers):
    tmp = [1,2,3,4,5,6,7,8,9,0]
    for n in numbers:
        if n in tmp:
            tmp.remove(n)
    
    return sum(tmp)

def solution(numbers):
    return 45 - sum(numbers)

numbers = [1,2,3,4,6,7,8,0]
print(solution(numbers))