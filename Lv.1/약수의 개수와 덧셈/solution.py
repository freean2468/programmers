# https://school.programmers.co.kr/learn/courses/30/lessons/77884?language=python3
import math

def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        answer += -n if math.sqrt(n).is_integer() else n
        
    return answer