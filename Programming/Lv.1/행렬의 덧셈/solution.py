# https://school.programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    # answer = []
    # for a1, a2 in zip(arr1, arr2):
    #     t = []
    #     for v1, v2 in zip(a1, a2):
    #         t.append(v1 + v2)
    #     answer.append(t)

    answer = [[v1 + v2 for v1, v2 in zip(a1, a2)] for a1, a2 in zip(arr1, arr2)]
        
    return answer