# https://school.programmers.co.kr/learn/courses/30/lessons/12916?language=python3
def solution(s):
    c = 0
    
    for l in s.lower():
        if l == 'p': c += 1
        elif l == 'y': c -= 1

    return True if c == 0 else False