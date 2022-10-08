# https://school.programmers.co.kr/learn/courses/30/lessons/120824
def solution(num_list):
    length = len(num_list)
    even_length = len(list(filter(lambda x:x % 2 == 0, num_list)))
    return [even_length, length - even_length]