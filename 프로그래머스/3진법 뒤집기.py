def solution(n):
    str_n = ''
    while n :
        str_n += str(n % 3)
        n = n // 3
    answer = int(str_n, 3)
    return answer