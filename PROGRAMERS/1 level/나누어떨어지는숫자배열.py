def solution(arr, divisor):
    
    return [-1] if len([num for num in arr if num % divisor == 0]) == 0 else sorted([num for num in arr if num % divisor == 0])

def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]

arr = [5, 9, 7, 10]
divisor = 5
print(solution(arr, divisor))