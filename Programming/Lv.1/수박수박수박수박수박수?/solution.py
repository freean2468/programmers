# https://school.programmers.co.kr/learn/courses/30/lessons/12922
def solution(n):
    return "수박" * int(n/2) + ("수" if n % 2 == 1 else "")