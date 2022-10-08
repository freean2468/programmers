# https://school.programmers.co.kr/learn/courses/30/lessons/120831
def solution(n):
    return sum(even for even in range(0, n + 1, 2))