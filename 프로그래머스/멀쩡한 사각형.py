def gcd(w, h):
    if w % h == 0:
        return h
    else:
        return gcd(h, w % h)

def solution(w,h):
    answer = w * h
    g = gcd(w,h)
    return answer - (w + h - g)