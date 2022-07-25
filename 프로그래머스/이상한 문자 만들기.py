def solution(s):
    answer = ''
    idx = 0
    for elem in s :
        if elem == ' ' :
            answer += ' '
            idx = 0
        else :
            if idx % 2 == 0 :
                answer += elem.upper()
            else : 
                answer += elem.lower()
            idx += 1
    return answer