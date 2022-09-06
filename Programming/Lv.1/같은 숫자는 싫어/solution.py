# https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3
def solution(arr):
    answer = []
    
    for i, a in enumerate(arr):
        if i == 0:
            answer.append(a)
        elif a != arr[i-1]:
            answer.append(a)
    
    return answer