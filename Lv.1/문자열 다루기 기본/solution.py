# https://school.programmers.co.kr/learn/courses/30/lessons/12918?language=python3
import re

def solution(s):    
    return True if re.search(r'^\d{4}$|^\d{6}$', s) else False

# isdigit 함수가 있ㅜㅏ.
# def alpha_string46(s):
#     return s.isdigit() and len(s) in (4, 6)