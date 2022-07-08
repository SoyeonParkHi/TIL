def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    both = set(lost) & set(reserve)
    lost = list(set(lost) - both)
    reserve = list(set(reserve) - both)
    lost_student = lost.copy()
    for i in lost_student :
        if i-1 in reserve :
            lost.remove(i)
            reserve.remove(i-1)
        elif i+1 in reserve :
            lost.remove(i)
            reserve.remove(i+1)
    return n - len(lost)