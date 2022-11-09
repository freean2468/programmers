# https://school.programmers.co.kr/learn/courses/30/lessons/120907
def solution(quiz): 
    return ["O" if eval(ev.replace("=", "==")) else "X" for ev in quiz]
