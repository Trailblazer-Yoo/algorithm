def solution(absolutes, signs):
    answer = 0
    for n, b in zip(absolutes, signs):
        if b == True:
            answer += n
        else:
            answer -= n
    
    return answer

def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

absolutes = [4,7,12]
signs = [True,False,True]