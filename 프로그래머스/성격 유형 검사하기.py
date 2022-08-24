def solution(survey, choices):
    score = dict(zip(['R','T','C','F','J','M','A','N'],[0]*8))
    answer = ''
    for i, j in zip(survey,choices) :
        if j in [1,2,3] :
            score[i[0]] += 4-j
        elif j in [5,6,7] :
            score[i[1]] += j-4
    for i,j in [('R','T'),('C','F'),('J','M'),('A','N')] :
        if score[i] == score[j] :
            answer += i
        else :
            answer += max(i,j,key = lambda x : score[x])
    return answer