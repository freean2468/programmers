# https://school.programmers.co.kr/learn/courses/30/lessons/120896
def solution(s):
    return ''.join(sorted([v for v in s if s.count(v) == 1]))
