# https://school.programmers.co.kr/learn/courses/30/lessons/120923
def solution(num, total):
    n = 0
    while 1:
        start = int(total / num) - int(num / 2)
        _ = list(range(start + n, start + num + n))
        if sum(_) == total:
            return _
        n += 1