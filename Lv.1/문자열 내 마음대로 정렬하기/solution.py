# https://school.programmers.co.kr/learn/courses/30/lessons/12915?language=python3
def solution(strings, n):
    strings.sort(key = lambda x : (x[n], x))
    return strings