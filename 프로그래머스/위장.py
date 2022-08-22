def solution(clothes):
    wear = dict()
    for cloth in clothes :
        if cloth[1] in wear :
            wear[cloth[1]] += 1
        else :
            wear[cloth[1]] = 1
    answer = 1
    for i in wear.values() :
        answer *= (i+1)
    return answer-1