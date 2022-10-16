# https://school.programmers.co.kr/learn/courses/30/lessons/120892
def solution(cipher, code):
    return ''.join([v for i, v in enumerate(list(cipher)) if (i + 1) % code == 0])
