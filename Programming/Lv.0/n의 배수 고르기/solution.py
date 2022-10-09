# https://school.programmers.co.kr/learn/courses/30/lessons/120905
def solution(n, numlist):
    return list(filter(lambda x:x % n == 0, numlist))
