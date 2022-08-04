# https://school.programmers.co.kr/learn/courses/30/lessons/12928
def solution(n):
    t = n
    for v in range (1, int(n / 2) + 1):
        if n % v == 0:
            t += v
    return t