# https://school.programmers.co.kr/learn/courses/30/lessons/120868
def solution(sides):
    sides.sort()
    return sides[1] - (sides[1] - sides[0]) + sides[0] - 1
