def solution(N, stages):
    fail_rate = dict()
    length = len(stages)
    for i in range(N) :
        if length == 0 :
            fail_rate[i + 1] = 0
        else : 
            temp = stages.count(i+1)
            fail_rate[i + 1] = temp / length
            length -= temp
    
    return sorted(fail_rate, key=lambda x: -fail_rate[x])