# https://school.programmers.co.kr/learn/courses/30/lessons/120849
def solution(my_string):
    return ''.join(list(filter(lambda x:x not in ['a', 'e', 'i', 'o', 'u'], my_string)))