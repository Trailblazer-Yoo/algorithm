def solution(arr1, arr2):

    return [[a1[i] + a2[i] for i in range(len(a1))] for a1, a2 in zip(arr1, arr2)]

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution(arr1, arr2))