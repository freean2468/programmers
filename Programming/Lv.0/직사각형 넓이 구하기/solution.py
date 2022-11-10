# https://school.programmers.co.kr/learn/courses/30/lessons/120860
def solution(dots):
    return (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1])
