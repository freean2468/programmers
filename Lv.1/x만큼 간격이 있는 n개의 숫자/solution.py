# https://school.programmers.co.kr/learn/courses/30/lessons/12954#
def solution(x, n):
    if x == 0:
        return [int(v) for v in list(str(x) * n)]
    else:
        return [v for v in range(x, x * (n + 1), x)]