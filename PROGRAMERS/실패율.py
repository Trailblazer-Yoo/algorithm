def solution(N, stages):
    arr = {}
    
    order = [i for i in range(1, (N + 1))]
    cur_stage = sorted(set(stages))
    for i in range(1, (N+1)):
        if i < min(cur_stage) or i > max(cur_stage):
            arr[i] = 0
            order.remove(i)

    for s in order:
        no = 0
        deno = 0
        for u in stages:
            if u >= s:
                deno += 1
            if s == u:
                no += 1
        if deno != 0:
            arr[s] = no/deno
        else:
            arr[s] = 0

    answer = sorted(arr.items(), key = lambda x: (-x[1], x[0]))

    return [i[0] for i in answer]

def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

N = 4
stages = [4,4,4,4,4]
print(solution(N, stages))