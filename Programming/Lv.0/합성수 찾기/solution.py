# https://school.programmers.co.kr/learn/courses/30/lessons/120846
def composition_number(n):
    count = 0
    for v in range(1, n + 1):
        if n % v == 0:
            count += 1
            
    if count >= 3:
        return n
    else:
        return 0

def solution(n):
    answer = 0
    for v in range(3, n + 1):
        answer += 1 if composition_number(v) != 0 else 0
    return answer
