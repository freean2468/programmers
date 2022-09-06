# https://school.programmers.co.kr/learn/courses/30/lessons/12982?language=python3
def solution(d, budget):
    answer = 0
    
    for v in sorted(d):
        if (budget - v < 0):
            break
            
        budget -= v
        answer += 1
    
    return answer