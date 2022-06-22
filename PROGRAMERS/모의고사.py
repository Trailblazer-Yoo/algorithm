def solution(answers):
    ans_1 = [1, 2, 3, 4, 5]
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    l = len(answers)
    if len(ans_1) >= l:
        ans_1 = ans_1[:l]
    else: 
        n, m = divmod(l, len(ans_1))
        ans_1 = ans_1 * n + ans_1[:m]
    if len(ans_2) >= l:
        ans_2 = ans_2[:l]
    else: 
        n, m = divmod(l, len(ans_2))
        ans_2 = ans_2 * n + ans_2[:m]
    if len(ans_3) >= l:
        ans_3 = ans_3[:l]
    else: 
        n, m = divmod(l, len(ans_3))
        ans_3 = ans_3 * n + ans_3[:m]

    tmp1 = [1 for x, y in zip(ans_1, answers) if x == y]
    tmp2 = [1 for x, y in zip(ans_2, answers) if x == y]
    tmp3 = [1 for x, y in zip(ans_3, answers) if x == y]

    tmp = [sum(tmp1), sum(tmp2), sum(tmp3)]
    max_t = max(tmp)
    if tmp.count(max_t) == 3:
        return [1,2,3]
    elif tmp.count(max_t) == 2:
        first = tmp.index(max_t) + 1
        tmp[tmp.index(max_t)] = 0
        second = tmp.index(max_t) + 1
        return [first, second]
    else:
        return [tmp.index(max_t) + 1]
    
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

answers = [1,2,3,4,5]
print(solution(answers))