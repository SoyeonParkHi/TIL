def solution(rows, columns, queries):
    answer = []
    nums = [[j*columns + i+1 for i in range(columns)] for j in range(rows)]
    for x1, y1, x2, y2 in queries :
        rot_num = []
        for i in range(x1-1,x2) :
            for j in range(y1-1,y2) :
                if i in [x1-1,x2-1] or j in [y1-1,y2-1] :
                    rot_num.append(nums[i][j])
        answer.append(min(rot_num))
        
        temp_min = nums[x1-1][y1-1]
        temp_max = nums[x2-1][y2-1]
        for i in range(x1-1,x2) :
            if i != x2-1 :
                nums[i][y1-1] = nums[i+1][y1-1]
            if i != x1-1 :
                nums[i][y2-1] = nums[i-1][y2-1]
        for j in range(y1-1,y2) :
            if j < y2-2 :
                nums[x2-1][j] = nums[x2-1][j+1]
            if j > y1 :
                nums[x1-1][j] = nums[x1-1][j-1]
        nums[x1-1][y1] = temp_min
        nums[x2-1][y2-2] = temp_max
    return answer