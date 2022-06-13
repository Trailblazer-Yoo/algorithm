T = int(input())
case_list = list(input().split() for _ in range(T))
for case in case_list:
    result = 0
    for c in case:
        try:
            result += float(c)
        except:
            if c == "@":
                result *= 3
            elif c == "%":
                result += 5
            else:
                result -= 7
    print(f'{result:.2f}')