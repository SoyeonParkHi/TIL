def solution(dartResult):
    score_list = [0,0,0]
    sq_list = ['S','D','T']
    temp = 0
    for i in range(3) :
        score = int(dartResult[temp])
        if score == 1 and dartResult[temp+1] == '0' :
            score = 10
            temp += 1
        sq = sq_list.index(dartResult[temp+1]) + 1
        score_list[i] = (score ** sq)
        if temp + 2 == len(dartResult) :
            break
        elif dartResult[temp+2] == '*' :
            score_list[i] *= 2
            if i != 0 :
                score_list[i-1] *= 2
            temp += 3
        elif dartResult[temp+2] == '#' :
            score_list[i] *= -1
            temp += 3
        else :
            temp += 2
    return sum(score_list)