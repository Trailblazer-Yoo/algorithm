while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    qu, re = divmod(a, b)
    if qu == 0 and re != 0:
        print('factor')
    elif qu != 0 and re == 0:
        print('multiple')
    else:
        print('neither')