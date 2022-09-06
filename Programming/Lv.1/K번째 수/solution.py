# https://school.programmers.co.kr/learn/courses/30/lessons/42748?language=python3
def solution(array, commands):
    answer = []
    for c in commands:
        sliced = array[c[0]-1:c[1]]
        sliced.sort()
        answer.append(sliced[c[2]-1])
        
    return answer