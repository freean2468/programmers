# https://school.programmers.co.kr/learn/courses/30/lessons/76501?language=python3
def solution(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        answer += a * (1 if s == True else -1)
    return answer