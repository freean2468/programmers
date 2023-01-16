# https://school.programmers.co.kr/learn/courses/30/lessons/131705#
def second(number, selected):
    answer = 0
    for i, n in enumerate(number):
        selected_2 = [_ for _ in selected]
        selected_2.append(n)
        if len(selected_2) == 3 and sum(selected_2) == 0:
            answer += 1
    return answer
    

def first(number, selected):
    answer = 0
    for i, n in enumerate(number):
        selected_2 = [_ for _ in selected]
        selected_2.append(n)
        answer += second(number[i + 1:], selected_2)
    return answer
        

def solution(number):
    answer = 0
    for i, n in enumerate(number):
        selected = [n]
        answer += first(number[i + 1:], selected)
    return answer
