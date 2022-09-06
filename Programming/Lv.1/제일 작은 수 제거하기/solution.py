# https://school.programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    al = len(arr)
    
    if al == 1:
        return [-1]
    
    arr.remove(min(arr))
    
    return arr