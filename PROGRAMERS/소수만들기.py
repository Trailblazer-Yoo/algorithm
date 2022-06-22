def solution(nums):
    result = []
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for z in range(j+1, len(nums)):
                tmp = nums[i] + nums[j] + nums[z]
                result.append(tmp)
    answer = []
    for tmp in result:
        for t in range(2, tmp):
            if tmp % t == 0:
                answer.append(tmp)
                break

    return len(result) - len(answer)

nums = [1,2,3,4]
print(solution(nums))