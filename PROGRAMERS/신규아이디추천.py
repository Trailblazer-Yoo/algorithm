import re

def solution(new_id):
    new_id = new_id.lower()
    print(new_id)
    new_id = re.sub('[^a-z0-9_.-]+', '', new_id)
    while True:
        if new_id == new_id.replace('..','.'):
            break
        else:
            new_id = new_id.replace('..','.')
    print(new_id, len(new_id))
    new_id = new_id.strip('.')
    if not new_id:
        new_id = 'a'
    if len(new_id) > 15:
        new_id = new_id[:15]
    new_id = new_id.strip('.')
    print(new_id, len(new_id))
    print(new_id)
    while len(new_id) < 3:
        new_id += new_id[-1]
    print(new_id)

    return new_id
    
new_id = "abcdefghijklmn.p"
print(solution(new_id))