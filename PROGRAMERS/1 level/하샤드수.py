def solution(x):
    deno = sum([int(i) for i in str(x)])
    return True if x % deno == 0 else False

x = 10
print(solution(x))