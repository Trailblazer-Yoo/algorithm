N = int(input())

result = 0
for _ in range(N):
    if input() == '1':
        result += 1
    else:
        result -= 1
print('Junhee is cute!' if result > 0 else 'Junhee is not cute!')