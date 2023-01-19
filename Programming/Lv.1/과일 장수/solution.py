# https://school.programmers.co.kr/learn/courses/30/lessons/135808
def quick_sort(_list):
    if len(_list) <= 1:
        return _list
    less, equal, greater = [], [], []
    pivot = _list[0]
    for n in _list:
        if n < pivot:
            less.append(n)
        elif n > pivot:
            greater.append(n)
        else:
            equal.append(n)
    return quick_sort(less) + equal + quick_sort(greater)
    

def solution(k, m, score):
    answer = 0
    score = list(reversed(quick_sort(score)))
    score = score[:len(score) // m * m]
    for i in range(1, len(score) // m + 1):
        answer += score[i * m - 1] * m
    return answer