def solution(array, commands):      

    return [sorted(array[com[0]-1:com[1]])[com[2] - 1] for com in commands]

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))