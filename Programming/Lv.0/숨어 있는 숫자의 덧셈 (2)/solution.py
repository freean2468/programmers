# https://school.programmers.co.kr/learn/courses/30/lessons/120864
def solution(my_string):
    split = (''.join([ch if ch.isnumeric() else ' ' for ch in my_string])).split()
    return sum(int(numeric) for numeric in split)
