# https://school.programmers.co.kr/learn/courses/30/lessons/120848
def solution(n):
    answer = 1
    acc = 1
    while acc <= n:
        answer += 1
        acc *= answer 
    return answer - 1
