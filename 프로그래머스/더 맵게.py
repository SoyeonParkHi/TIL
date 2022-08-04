import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(scoville[0] < K) :
        if len(scoville) < 2 :
            return -1
        a = heapq.heappop(scoville) + 2*heapq.heappop(scoville)
        heapq.heappush(scoville, a)
        answer += 1
    return answer