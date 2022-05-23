def solution(N, stages):
    answer = []
    fail = {}
    stages.sort()
    player = len(stages)
    stage_num = list(set(stages))
    
    for i in range(N):
        fail[i+1] = 0

    for i in range(len(stage_num)):
        if stage_num[i] > N:
            break
        num = stages.count(stages[i])
        fail[stage_num[i]] = num/player
        player -= num

    fail = sorted(fail.items(), key=lambda values : values[1], reverse=True)

    for i in fail:
        answer.append(i[0])
    
    return answer

N = int(input())
stages = list(map(int, input().split()))
print(solution(N, stages))