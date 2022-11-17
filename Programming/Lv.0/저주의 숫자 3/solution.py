# https://school.programmers.co.kr/learn/courses/30/lessons/120871#
def solution(n):
    num = 0
    for _ in range(1, n + 1):
        num += 1
        while '3' in str(num) or num % 3 == 0:
            num += 1
    return num
