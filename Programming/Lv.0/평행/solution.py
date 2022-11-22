# https://school.programmers.co.kr/learn/courses/30/lessons/120875
def solution(dots):
    for d in range(len(dots)):
        for i in range(d, len(dots)):
            i1 = (i + d) % len(dots)
            i2 = (i + d + 1) % len(dots)
            dydx1 = (((dots[i1][1] - dots[i2][1]) ** 2) / ((dots[i1][0] - dots[i2][0]) ** 2)) ** 0.5
            i3 = (i + d + 2) % len(dots)
            i4 = (i + d + 3) % len(dots)
            dydx2 = (((dots[i3][1] - dots[i4][1]) ** 2) / ((dots[i3][0] - dots[i4][0]) ** 2)) ** 0.5
            
            if dydx1 == dydx2:
                return 1
    
    return 0
