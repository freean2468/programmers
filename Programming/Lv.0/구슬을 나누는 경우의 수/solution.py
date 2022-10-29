# https://school.programmers.co.kr/learn/courses/30/lessons/120840
def factorial(n):
    answer = 1
    for v in range(1, n + 1):
        answer *= v
    return answer
    

def solution(balls, share):
    return factorial(balls) / (factorial(balls-share) * factorial(share))
