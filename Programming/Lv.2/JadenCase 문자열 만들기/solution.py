# https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    first = True
    s = [v for v in s.lower()]
    for i, c in enumerate(s):
        if first:
            s[i] = s[i].upper()
            first = False
        if c == ' ':
            first = True
    
    return ''.join(s)