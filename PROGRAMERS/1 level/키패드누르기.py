def solution(numbers, hand):
    answer = ''
    l = 10
    r = 12
    while numbers:
        n = numbers.pop(0)
        if n == 0:
            n = 11
            
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            l = n
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            r = n
        else:
            s_x, s_y = divmod((n - 1), 3)
            l_x, l_y = divmod((l - 1), 3)
            r_x, r_y = divmod((r - 1), 3)
            l_xy = abs(l_x - s_x) + abs(l_y - s_y)
            r_xy = abs(r_x - s_x) + abs(r_y - s_y)
            if l_xy < r_xy :
                answer += 'L'
                l = n
            elif l_xy > r_xy:
                answer += 'R'
                r = n
            else:
                if hand == 'right':
                    answer += 'R'
                    r = n
                elif hand == 'left':
                    answer += 'L'
                    l = n

    return answer

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))