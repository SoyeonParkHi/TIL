def solution(s, n):
    answer = ''
    for s_elem in s :
        if s_elem == ' ' :
            answer += ' '
        else :
            add_ans = ord(s_elem) + n
            if (ord(s_elem) <= 90 and add_ans > 90) or (ord(s_elem) <= 122 and add_ans > 122) :
                add_ans -= 26
            answer += chr(add_ans)
    return answer