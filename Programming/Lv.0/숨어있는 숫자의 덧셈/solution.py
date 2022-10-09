# https://school.programmers.co.kr/learn/courses/30/lessons/120851
def solution(my_string):
    numeric_list = list(map(str, [v for v in range(1, 10)]))
    answer = 0
    for v in list(my_string):
        if v in numeric_list:
            answer += int(v)
    return answer
