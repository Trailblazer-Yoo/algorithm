def solution(s, n):
    low = ['a','b','c','d','e','f','g','h','i','j',
           'k','l','m','n','o','p','q','r','s','t',
           'u','v','w','x','y','z']
    upper = [i.upper() for i in low]
    tmp = []
    for i in s:
        if i in low:
            tmp.append(low[(low.index(i)+n) % len(low)])
        elif i in upper:
            tmp.append(upper[(upper.index(i)+n) % len(upper)])
        else:
            tmp.append(i)
    return ''.join(tmp)
    
s = "a B z"
n = 1
print(solution(s, n))