# https://school.programmers.co.kr/learn/courses/30/lessons/120886#
def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0
