# https://school.programmers.co.kr/learn/courses/30/lessons/12924
def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        t = 0
        while t < n:
            t += i
            i += 1
        
        if t == n:
            answer += 1
        
    return answer