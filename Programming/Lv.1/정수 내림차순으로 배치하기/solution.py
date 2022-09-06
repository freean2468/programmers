# https://school.programmers.co.kr/learn/courses/30/lessons/12933
def solution(n):
    answer = []
    while n > 0:
        answer.append(str(n % 10))
        n //= 10
        
    return int(''.join(sorted(answer, reverse=True)))