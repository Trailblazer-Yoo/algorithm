def solution(lottos, win_nums):
    dict_order = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}
    l = 0
    for num in win_nums:
        if num in lottos:
            lottos.remove(num)
            l += 1
    
    answer = [dict_order[lottos.count(0) + l], dict_order[l]]
    return answer

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))