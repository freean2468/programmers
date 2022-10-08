# https://school.programmers.co.kr/learn/courses/30/lessons/120816#
def solution(slice_, n):
    d, m = divmod(n, slice_)
    return d + int(m != 0)
