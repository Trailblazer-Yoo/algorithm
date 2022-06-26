def solution(w,h):
    c, d = max(w, h), min(w, h)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    return w * h - (w + h - c)

w = 8
h = 12
print(solution(w,h))