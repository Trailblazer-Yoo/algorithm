def solution(strings, n):
    strings = {i : i[n] for i in strings}
    strings = sorted(strings.items(), key = lambda x: (x[1], x[0])) 
    return [s[0] for s in strings]

strings = ["abce", "abcd", "cdx"]
n = 2
print(solution(strings, n))