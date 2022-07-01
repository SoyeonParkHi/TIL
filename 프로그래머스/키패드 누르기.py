def solution(numbers, hand):
    answer = ''
    num_hand = {'L' : 10, 'R' : 12, 'left' : 'L', 'right' : 'R'}
    distance = [0, 'nothing', 1, 3, 2, 4, 6, 5, 7, 9, 8, 10]
    
    for num in numbers :
        if num != 0 and num % 3 == 0 :
            answer += 'R'
            num_hand['R'] = num
        elif num % 3 == 1 :
            answer += 'L'
            num_hand['L'] = num
        else :
            if num == 0 :
                num = 11
            L_distance = (distance.index(abs(num_hand['L'] - num)) - 1) // 3
            R_distance = (distance.index(abs(num_hand['R'] - num)) - 1) // 3
            if L_distance == R_distance :
                answer += num_hand[hand]
                num_hand[num_hand[hand]] = num
            elif L_distance < R_distance : 
                answer += 'L'
                num_hand['L'] = num
            else : 
                answer += 'R'
                num_hand['R'] = num
    return answer