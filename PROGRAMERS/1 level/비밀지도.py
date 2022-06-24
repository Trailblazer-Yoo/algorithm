def solution(n, arr1, arr2):
    wall1 = []
    for num in arr1:
        tmp = ''
        while num:
            tmp += str(num % 2)
            num = num // 2
        tmp = tmp[::-1]
        if len(tmp) < n:
            wall1.append((n-len(tmp)) * '0' + tmp)
        else:
            wall1.append(tmp)
            
    wall2 = []
    for num in arr2:
        tmp = ''
        while num:
            tmp += str(num % 2)
            num = num // 2
        tmp = tmp[::-1]
        if len(tmp) < n:
            wall2.append((n-len(tmp)) * '0' + tmp)
        else:
            wall2.append(tmp)
    

    answer = []
    for n1, n2 in zip(wall1, wall2):
        tmp = ''
        for i in range(n):
            if n1[i] == '1' or n2[i] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
                
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))