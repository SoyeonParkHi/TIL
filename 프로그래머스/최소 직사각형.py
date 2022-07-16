def solution(sizes):
    max_len, min_len = 0, 0
    for size in sizes :
        if max(size[0], size[1]) > max_len :
            max_len = max(size[0], size[1])
        if min(size[0], size[1]) > min_len :
            min_len = min(size[0], size[1])
    return max_len * min_len