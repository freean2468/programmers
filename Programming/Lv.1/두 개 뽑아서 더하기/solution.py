# https://school.programmers.co.kr/learn/courses/30/lessons/68644?language=python3
from itertools import combinations

def solution(numbers):
    return sorted(set([v[0] + v[1] for v in combinations(numbers, 2)]))