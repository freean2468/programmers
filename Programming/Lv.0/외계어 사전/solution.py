# https://school.programmers.co.kr/learn/courses/30/lessons/120869
def solution(spell, dic):
    for word in filter(lambda x:len(x) == len(spell), dic):
        for ch in spell:
            word = word.replace(ch, '', 1)
            
        if word == '':
            return 1
        
    return 2
