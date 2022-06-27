import sys

input = lambda : sys.stdin.readline()

n = int(input())
k = int(input())
list_card = [input() for i in range(n)]

array = set()
def makeCom(cnt, perm, visit):
    if cnt ==k:
        array.add(''.join(perm))
        return
    
    for i in range(n):
        if not visit[i]:
            
    
