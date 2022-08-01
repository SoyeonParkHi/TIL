def solution(s):
    len_list = [len(s)]
    for i in range(1, len(s) // 2 + 1) :
        length = len(s)
        temp = 1
        for j in range(0,len(s),i) :
            if s[j:j + i] == s[j+i:j+2*i] :
                temp += 1
            else:
                if temp > 1 :
                    length -= (temp-1) * i - (len(str(temp)))
                    temp = 1
        len_list.append(length)
    return min(len_list)