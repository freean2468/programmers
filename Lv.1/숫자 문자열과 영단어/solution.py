# https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=python3
import re

def solution(s):
    en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, v in enumerate(en):
        s = re.sub(v, str(i), s)
    return int(''.join(s))