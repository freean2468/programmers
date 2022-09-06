# https://school.programmers.co.kr/learn/courses/30/lessons/12925
def solution(s):
    return int(s) if s.isdigit() else int(s[1:]) * (1 if s[0] == '+' else -1)