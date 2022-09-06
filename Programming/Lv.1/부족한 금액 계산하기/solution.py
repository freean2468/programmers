# https://school.programmers.co.kr/learn/courses/30/lessons/82612?language=python3
def solution(price, money, count):
    for i in range(1, count + 1):
        money -= price * i
        
    return -money if money < 0 else 0

# 등차수열의 합을 구하는 방식으로 접근할 수 있다.
# 공차가 price니까. 
# (count * ((2 * price) + (count - 1) * price)) / 2

# t = ((count * ((2 * price) + (count - 1) * price)) / 2)
# money -= t
# return -money if money < 0 else 0