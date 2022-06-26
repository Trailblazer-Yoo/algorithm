def solution(sizes):
    hor = 0
    ver = 0
    for i, size in enumerate(sizes):
        if size[0] < size[1]:
            sizes[i] = [size[1], size[0]]
    for size in sizes:
        hor = max(hor, size[0])
        ver = max(ver, size[1])

    answer = hor * ver
    return answer

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))