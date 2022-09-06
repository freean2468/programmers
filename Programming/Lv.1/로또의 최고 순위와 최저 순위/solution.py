# https://school.programmers.co.kr/learn/courses/30/lessons/77484?language=python3
def solution(lottos, win_nums):
    valid = [v for v in lottos if v != 0]
    zero = [v for v in lottos if v == 0]

    hit = 0
    for v in valid:
        if v in win_nums:
            hit += 1

    max_hit = hit + len(zero)

    return [min(7 - max_hit, 6), min(7 - hit, 6)]
