# https://school.programmers.co.kr/learn/courses/30/lessons/120818#
def solution(price):
    db = [
        (500000,0.2),
        (300000,0.1),
        (100000,0.05)
    ]
    
    for v in db:
        if price >= v[0]:
            return int(price - price * v[1])
    
    return price