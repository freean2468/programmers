# https://school.programmers.co.kr/learn/courses/30/lessons/120845
def solution(box, n):
    volume = 1
    for v in box:
        volume *= (v // n)
    return volume
