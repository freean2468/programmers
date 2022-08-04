# https://school.programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    o = x
    t = 0
    
    while x > 0:
        t = t + (x % 10)
        x //= 10
        
    return True if o % t == 0 else False