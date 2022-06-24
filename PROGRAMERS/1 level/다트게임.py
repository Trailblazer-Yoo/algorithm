def solution(dartResult):
    dartResult = list(dartResult)
    list_dartResult = []
    for i, char in enumerate(dartResult):
        try:
            num = int(char)
            try:
                num2 = int(dartResult[i+1])
                num2 = dartResult.pop(i+1)
                list_dartResult.append(int(char + num2))
            except:
                list_dartResult.append(num)
        except:
            list_dartResult.append(char)

            
    tmp = []
    cnt = -1
    while list_dartResult:
        com = list_dartResult.pop(0)

        try:
            com = int(com)
            tmp.append(com)
            cnt += 1
        except:
            if com == "S":
                tmp[cnt] = tmp[cnt] ** 1
            elif com == "D":
                tmp[cnt] = tmp[cnt] ** 2
            elif com == "T":
                tmp[cnt] = tmp[cnt] ** 3
            elif com == "*":
                tmp[cnt] = tmp[cnt] * 2
                if cnt > 0: 
                    tmp[cnt-1] = tmp[cnt-1] * 2
            elif com == "#":
                tmp[cnt] = tmp[cnt] * (-1)

    return sum(tmp)

def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)

dartResult = "1D2S#10S"
print(solution(dartResult))
