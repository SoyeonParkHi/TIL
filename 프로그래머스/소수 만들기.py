from itertools import combinations

def solution(nums):
    sum_nums = [sum(i) for i in combinations(nums, 3)]
    
    answer = 0
    for j in sum_nums :
        for k in range(2, j) :
            if j % k == 0 :
                break
        else : answer += 1
    return answer