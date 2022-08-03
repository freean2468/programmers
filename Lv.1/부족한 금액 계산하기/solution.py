# https://school.programmers.co.kr/learn/courses/30/lessons/82612?language=python3
def solution(price, money, count):
    for i in range(1, count + 1):
        money -= price * i
        
    return -money if money < 0 else 0