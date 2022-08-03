# https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3
def solution(sizes):
    sizes = [[min(s[0], s[1]), max(s[0], s[1])] for s in sizes]
    return max([s[0] for s in sizes]) * max([s[1] for s in sizes])