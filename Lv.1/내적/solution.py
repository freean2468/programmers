# https://school.programmers.co.kr/learn/courses/30/lessons/70128?language=python3
def solution(a, b):
    return sum(an * bn for an, bn in zip(a, b))