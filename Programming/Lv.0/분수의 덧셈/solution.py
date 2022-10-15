# https://school.programmers.co.kr/learn/courses/30/lessons/120808
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while(b != 0):
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


def solution(denum1, num1, denum2, num2):
    max_ = max(num1, num2)
    min_ = min(num1, num2)
    
    denominator = max_ if max_ % min_ == 0 else lcm(num1, num2)
    
    denum1 *= (denominator / num1)
    denum2 *= (denominator / num2)
    
    numerator = denum1 + denum2
    gcd_ = gcd(numerator, denominator)
    
    return [numerator / gcd_, denominator / gcd_]
