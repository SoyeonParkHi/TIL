def solution(a, b):
    month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    md = (sum(month_day[:a-1]) + b) % 7
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    return day[md]