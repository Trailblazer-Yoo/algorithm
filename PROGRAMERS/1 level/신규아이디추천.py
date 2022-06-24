import re

def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    new_id = re.sub('[^a-z0-9_.-]+', '', new_id)
    
    # 3단계
    while True:
        if new_id == new_id.replace('..','.'):
            break
        else:
            new_id = new_id.replace('..','.')
    
    # 4단계
    new_id = new_id.strip('.')
    
    # 5단계
    if not new_id:
        new_id = 'a'
        
    # 6단계
    if len(new_id) > 15:
        new_id = new_id[:15]
    new_id = new_id.strip('.')
    
    # 7단계
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id
    
new_id = "abcdefghijklmn.p"
print(solution(new_id))