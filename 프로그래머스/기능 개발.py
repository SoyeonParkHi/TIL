import math
def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)) :
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    answer = []
    temp = days[0]
    cnt = 1
    for j in range(1, len(days)) :
        if temp < days[j] :
            answer.append(cnt)
            temp = days[j]
            cnt = 1
        else : 
            cnt += 1
    answer.append(cnt)
    return answer