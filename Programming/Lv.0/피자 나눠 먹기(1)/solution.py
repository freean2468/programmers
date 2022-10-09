# https://school.programmers.co.kr/learn/courses/30/lessons/120814
def solution(n):
    d, m = divmod(n, 7)
    return d + int(m != 0)