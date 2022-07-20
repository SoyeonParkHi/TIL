def solution(arr):
    answer = []
    temp = 10
    for num in arr :
        if num != temp :
            answer.append(num)
            temp = num
    return answer