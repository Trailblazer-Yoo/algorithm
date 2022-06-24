def solution(sizes):
    hor = 0
    ver = 0
    for i, size in enumerate(sizes):
        if size[0] < size[1]:
            sizes[i] = [size[1], size[0]]
    for size in sizes:
        hor = max(hor, size[0])
        ver = max(ver, size[1])
    print(sizes)
    print(hor, ver)
    answer = 0
    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))