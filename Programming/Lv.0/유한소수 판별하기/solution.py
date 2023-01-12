def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while True:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r
    

def solution(a, b):
    _gcd = gcd(a, b)
    a /= _gcd
    b /= _gcd
    if a % b == 0:
        return 1
    while b % 2 == 0:
        b /= 2
    while b % 5 == 0:
        b /= 5
    return 1 if b == 1 else 2