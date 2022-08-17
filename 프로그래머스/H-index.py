def solution(citations):
    citations.sort()
    for i in range(len(citations),0,-1) :
        if citations[len(citations)-i] >= i :
            return i
    return 0

'''
프로그래머스 다른 풀이
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
'''