# https://school.programmers.co.kr/learn/courses/30/lessons/17681?language=python3
def solution(n, arr1, arr2):
    map = []
    for a1, a2 in zip(arr1, arr2):
        binary = bin(a1 | a2)[2:].zfill(n)
        
        map.append(''.join(['#' if b == "1" else ' ' for b in binary]))
    
    return map