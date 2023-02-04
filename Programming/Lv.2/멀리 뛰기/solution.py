# https://school.programmers.co.kr/learn/courses/30/lessons/12914#
def solution(n):
    answer = 0
    r = 0
    while r * 2 <= n:
        numerator = 1
        denominator = 1
        shrinked_n = n - r
        for _ in range(shrinked_n - r + 1, shrinked_n + 1):
            numerator *= _
        for _ in range(1, r + 1):
            denominator *= _
        r += 1
        answer += numerator // denominator
    return answer % 1234567