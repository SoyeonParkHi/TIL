def solution(n, arr1, arr2):
    answer = []
    sum_arr = []
    for i in range(n) :
        arr1[i] = bin(arr1[i])[2:]
        arr2[i] = bin(arr2[i])[2:]
        sum_arr.append(int(arr1[i]) + int(arr2[i]))
        print(sum_arr[i])
        temp = ''
        for j in str(sum_arr[i]) :
            temp += '#' if int(j) else ' '
        if len(temp) < n :
            temp = ' ' * (n - len(temp)) + temp
        answer.append(temp)
    return answer