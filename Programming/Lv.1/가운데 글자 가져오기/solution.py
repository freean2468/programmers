# https://school.programmers.co.kr/learn/courses/30/lessons/12903?language=python3
def solution(s):
    m = len(s) // 2
    return s[m-1:m+1] if len(s) % 2 == 0 else s[m:m+1]