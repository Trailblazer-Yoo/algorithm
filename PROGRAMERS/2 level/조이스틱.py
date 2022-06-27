from idna import alabel


def solution(name):
    init_name = 'A'* len(name)
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    cursor = 0
    for i, char in enumerate(name):
        if init_name[i] == char:
            continue
        
            
    return answer

name = "JEROEN"
print(solution(name))