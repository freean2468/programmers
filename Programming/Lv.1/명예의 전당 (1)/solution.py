# https://school.programmers.co.kr/learn/courses/30/lessons/138477
def solution(k, score):
    answer = []
    acc = []
    for s in score:
        if len(acc) < k:
            acc.append(s)
            acc.sort()
            answer.append(acc[0])
        else:
            if acc[0] < s:
                acc[0] = s
                acc.sort()
            answer.append(acc[0])
    return answer