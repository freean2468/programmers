# https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, p in enumerate(participant):
        if i >= len(completion) or completion[i] != p:
            return p