# https://school.programmers.co.kr/learn/courses/30/lessons/120826
def solution(my_string, letter):
    return ''.join(list(filter(lambda x:x != letter, list(my_string))))
    