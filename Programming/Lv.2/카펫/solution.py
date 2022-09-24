# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    t = brown + yellow
    
    for height in range(3, t):
        width = t / height
        if height * width == t and (width - 2) * (height - 2) == yellow:
            return [width, height]
