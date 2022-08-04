# https://school.programmers.co.kr/learn/courses/30/lessons/12918?language=python3
import re

def solution(s):    
    return True if re.search(r'^\d{4}$|^\d{6}$', s) else False