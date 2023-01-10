# https://school.programmers.co.kr/learn/courses/30/lessons/120884
def solution(chicken):
    service = 0
    remainder = 0
    while chicken > 9:
        remainder += chicken % 10
        service += chicken // 10
        chicken //= 10
    remainder += chicken
    while remainder >= 10:
        service += remainder // 10
        remainder = remainder // 10 + remainder % 10
    return service