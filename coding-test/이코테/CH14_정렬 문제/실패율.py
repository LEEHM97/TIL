def solution(N, stages):
    answer = []
    player = len(stages)
    
    for i in range(1, N+1):
        num = stages.count(stages[i])
        
        if player == 0:
            fail_rate = 0
        else:
            fail_rate = num/player

        answer.append((i, fail_rate))
        player -= num

    answer = sorted(answer, key=lambda values : values[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer

N = int(input())
stages = list(map(int, input().split()))
print(solution(N, stages))