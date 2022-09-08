# https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=python3
def solution(s):
    arr = sorted([int(v) for v in s.split(' ')])
    return ' '.join([str(arr[0]), str(arr[-1])])