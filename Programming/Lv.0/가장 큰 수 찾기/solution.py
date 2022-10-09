# https://school.programmers.co.kr/learn/courses/30/lessons/120899
def solution(array):
    max_ = max(array)
    return [max_, array.index(max_)]