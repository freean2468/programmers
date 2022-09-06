# https://school.programmers.co.kr/learn/courses/30/lessons/17682?language=python3
import re

def solution(dartResult):
    bonuses = {'S': 1, 'D': 2, 'T': 3}
    options = {'*': 2, '#': -1, '': 1}
    answer = []
    matched = re.findall(r'(\d{0,})(\w)([\*\#]{0,})', dartResult)
    for i, m in enumerate(matched):
        o = m[2]
        if o == '*' and 0 < len(answer):
            answer[i-1] *= options[o]
        answer.append(int(m[0]) ** bonuses[m[1]] * options[o])
        
    return sum(answer)