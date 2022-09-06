# https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i, p in enumerate(participant):
        if i >= len(completion) or completion[i] != p:
            return p

# collections 모듈이 있구나
# 심지어 Counter class는 subtraction 연산까지 지원해주네.
# import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]