# https://school.programmers.co.kr/learn/courses/30/lessons/12949
def solution(arr1, arr2):
    answer = []
    for m in range(len(arr1)):
        answer.append([])
        for n in range(len(arr2[0])):
            s = 0
            for i in range(len(arr2)):
                s += arr1[m][i] * arr2[i][n]
            answer[m].append(s)
    return answer