import sys

input = lambda: sys.stdin.readline().strip()
T = int(input())
storage = [list(map(int, input().split())) for _ in range(T)]
for case in storage:
    N = case[0]
    if N == 1:
        pass
    else:
        temp = {}
        deno = 2
        while N != 1:
            if N % deno == 0:
                N /= deno
                if deno not in temp:
                    temp[deno] = 1
                else:
                    temp[deno] += 1
            else:
                deno += 1
    M = case[1]
    if M == 1:
        pass
    else:
        deno = 2
        count = 0
        while M != 1:
            if M % deno == 0:
                M /= deno
                count += 1
                if temp[deno] < count:
                    temp[deno] = count
            else:
                deno += 1
    result = 1
    try:
        for a, b in temp.items():
            result *= a ** b
            print(result)
    except:
        print(max(case))
