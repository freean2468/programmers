# https://school.programmers.co.kr/learn/courses/30/lessons/68935?language=python3
import numpy

def solution(n):
    return int(numpy.base_repr(n, base=3)[::-1], 3)