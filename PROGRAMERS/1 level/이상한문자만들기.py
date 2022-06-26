def solution(s):
    answer = []
    words = s.split(" ")
    for word in words:
        w = ""
        for i in range(len(word)):
            if i % 2:
                w += word[i].lower()
            else:
                w += word[i].upper()
        answer.append(w)
    return ' '.join(answer)

def solution(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

s = "try hello world"
print(solution(s))