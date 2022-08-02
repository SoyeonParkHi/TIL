def solution(record):
    answer = []
    id_name = dict()
    
    for rec in record :
        rec_split = rec.split()
        if rec_split[0] in ['Enter', 'Change'] :
            id_name[rec_split[1]] = rec_split[2]
    
    for rec in record :
        rec_split = rec.split()
        if rec_split[0] == 'Enter' :
            answer.append(f'{id_name[rec_split[1]]}님이 들어왔습니다.')
        elif rec_split[0] == 'Leave' :
            answer.append(f'{id_name[rec_split[1]]}님이 나갔습니다.')
    return answer