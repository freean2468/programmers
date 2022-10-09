# https://school.programmers.co.kr/learn/courses/30/lessons/120839
def solution(rsp):
    winning = {
        '2': '0',
        '0': '5',
        '5': '2'
    }
    
    return ''.join(list(map(lambda x:winning[x], list(rsp))))
