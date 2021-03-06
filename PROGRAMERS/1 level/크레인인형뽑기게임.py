def solution(board, moves):
    box = []
    b_row = len(board)
    
    answer = 0
    while moves:
        col = moves.pop(0) - 1
        row = 0
        
        while True:
            if row == b_row:
                break
            
            elif board[row][col] != 0:
                num = board[row][col]
                board[row][col] = 0
                if len(box) > 0 and box[-1] == num:
                    box.pop()
                    answer += 2
                else:
                    box.append(num)
                break
            
            row += 1

    return answer


def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    print(cols)
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
print(zip(*board))
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
# 4 1 2 2 1 3 4