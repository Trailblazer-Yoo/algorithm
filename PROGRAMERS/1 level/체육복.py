def solution(n, lost, reserve):
    res = set(reserve) - set(lost)
    los = set(lost) - set(reserve)
            
    for l in los:
        if (l - 1) in res:
            res.remove(l-1)
        elif (l + 1) in res:
            res.remove(l+1)
        else:
            n -= 1

    return n

n = 5
lost = [2,3, 4]
reserve = [1, 3, 5]
print(reserve)
print(solution(n, lost, reserve))