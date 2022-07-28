def solution(n):
    num124 = [1,2,4]
    answer = ''
    while n > 0 :
        answer = str(num124[int(n % 3) - 1]) + answer
        if n % 3 == 0 :
            n -= 3
        n = (n - n % 3) / 3
    return answer