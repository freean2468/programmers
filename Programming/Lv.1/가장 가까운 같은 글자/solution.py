# https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    answer = []
    db = {}
    for i, c in enumerate(s):
        if c in db:
            answer.append(i - db[c])
        else:
            answer.append(-1)
        db[c] = i
    return answer