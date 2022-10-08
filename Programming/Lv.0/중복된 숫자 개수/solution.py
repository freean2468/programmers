# https://school.programmers.co.kr/learn/courses/30/lessons/120583
def solution(array, n):
    return len(list(filter(lambda x:x == n, array)))