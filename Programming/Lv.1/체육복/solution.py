# https://school.programmers.co.kr/learn/courses/30/lessons/42862?language=python3
def solution(n, lost, reserve):
    lf = [n for n in lost if n not in reserve]
    rf = [n for n in reserve if n not in lost]
    
    for l in lf[:]:
        pr = l - 1
        ne = l + 1
        
        if pr in rf and ne in rf:
            continue
        elif pr in rf:
            del rf[rf.index(pr)]
            del lf[lf.index(l)]
        elif ne in rf:
            del rf[rf.index(ne)]
            del lf[lf.index(l)]
            
    for l in lf[:]:
        pr = l - 1
        ne = l + 1
        
        if pr in rf:
            del rf[rf.index(pr)]
            del lf[lf.index(l)]
        elif ne in rf:
            del rf[rf.index(ne)]
            del lf[lf.index(l)]
    
    return n - len(lf)