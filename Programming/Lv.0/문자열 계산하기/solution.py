# https://school.programmers.co.kr/learn/courses/30/lessons/120902
def solution(my_string):
    return sum([int(n) for n in my_string.replace(' - ', ' + -').split(' + ')])
