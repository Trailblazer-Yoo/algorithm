def solution(nums):
    N = len(nums)
    if len(set(nums)) >= N//2:
        return N//2
    else:
        return len(set(nums))
    
def solution(ls):
    return min(len(ls)/2, len(set(ls)))

nums = [3,1,2,3]
solution(nums)