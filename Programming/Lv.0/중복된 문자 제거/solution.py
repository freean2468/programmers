# https://school.programmers.co.kr/learn/courses/30/lessons/120888
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
