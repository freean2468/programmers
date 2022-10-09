# https://school.programmers.co.kr/learn/courses/30/lessons/120837
def solution(hp):
    d1, m = divmod(hp, 5)
    d2, m = divmod(m, 3)
    d3 = m / 1
    return d1 + d2 + d3