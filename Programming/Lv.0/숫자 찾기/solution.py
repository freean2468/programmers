# https://school.programmers.co.kr/learn/courses/30/lessons/120904
def solution(num, k):
    try:
        return str(num).index(str(k)) + 1
    except ValueError:
        return -1
