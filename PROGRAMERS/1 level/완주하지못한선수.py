# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
    
    
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
    
#     return participant[-1]

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
    
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))