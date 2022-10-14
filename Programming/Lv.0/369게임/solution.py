# https://school.programmers.co.kr/learn/courses/30/lessons/120891
def solution(order):
    return len([v for v in list(str(order)) if v in ['3', '6', '9']])
