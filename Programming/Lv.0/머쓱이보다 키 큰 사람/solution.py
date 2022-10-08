# https://school.programmers.co.kr/learn/courses/30/lessons/120585
def solution(array, height):
    return len(list(filter(lambda x:x > height, array)))