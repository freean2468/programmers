# https://school.programmers.co.kr/learn/courses/30/lessons/120825
def solution(my_string, n):
    return ''.join(list(map(lambda x:x*n, list(my_string))))