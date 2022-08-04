# https://school.programmers.co.kr/learn/courses/30/lessons/12934
def solution(n):
    x = n ** 0.5
    if x.is_integer():
        return (x+1) ** 2
    else:
        return -1