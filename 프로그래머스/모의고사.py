def solution(answers):
    winner = []
    answer_123 = [0, 0, 0]
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_3 = [3, 1, 2, 4, 5]
    for i in range(len(answers)) :
        if answers[i] == i % 5 + 1 :
            answer_123[0] += 1
        if answers[i] == answer_2[i % 8] :
            answer_123[1] += 1
        if answers[i] == answer_3[(i // 2) % 5] :
            answer_123[2] += 1
    
    for j in range(3) :
        if answer_123[j] == max(answer_123) :
            winner.append(j + 1)
    return winner