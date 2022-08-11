# https://school.programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = []
    
    s = sorted(list(map(lambda x: '%s%s' % (x, '}'),s[1:len(s) - 2].split('},'))), key=lambda x: len(x))
    
    for e in s:
        r = list(filter(lambda x: x not in answer, e[1:len(e) - 1].split(',')))
        answer.append(r[0])
    
    return list(map(lambda x: int(x), answer))

# Counter 활용
# def solution(s):

# s = Counter(re.findall('\d+', s))
# return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

# import re
# from collections import Counter