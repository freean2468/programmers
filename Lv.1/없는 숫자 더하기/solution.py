# https://school.programmers.co.kr/learn/courses/30/lessons/86051?language=python3
def solution(numbers):
    t = 9 * 10 / 2
    for n in numbers:
        t -= n
    return t