# https://school.programmers.co.kr/learn/courses/30/lessons/12899
c = ['1', '2', '4']

def ex(n):
    three_count = (n - 1) // 3
    
    # print(n, three_count)
    
    if three_count == 0:
        return c[2] if n % 3 == 0 else c[int(n % 3) - 1]
    else:
        return ex(three_count) + c[int(n % 3) - 1]
    
def solution(n):
    return ex(n)