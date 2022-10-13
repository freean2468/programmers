# https://school.programmers.co.kr/learn/courses/30/lessons/120836
def solution(n):
    answer = 0
    
    for v in range(1, n + 1):
        if (n / v).is_integer():            
            if (n / v) == v:
                return (answer + 1) * 2 - 1
            elif (n / v) < v:
                return answer * 2
            
            answer += 1
