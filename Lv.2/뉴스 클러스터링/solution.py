# https://school.programmers.co.kr/learn/courses/30/lessons/17677
import re

def pairwise(l):
    nl = []
    for i, n in enumerate(l):
        if i < len(l) - 1:
            p = n+l[i+1]
            m = re.findall('^[a-z][a-z]$', p)
            if m:
                nl.append(p)
    return nl

def intersection(l1, l2):
    nl = []
    s = set(l1 + l2)
    
    for c in s:
        for i in range(min(l1.count(c), l2.count(c))):
            nl.append(c)
            
    return nl

def union(l1, l2):
    nl = []
    s = set(l1 + l2)
    
    for c in s:
        for i in range(max(l1.count(c), l2.count(c))):
            nl.append(c)
            
    return nl

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    if str1 == str2:
        return 65536
    
    comb1 = list(map(lambda x:''.join(x), pairwise(str1)))
    comb2 = list(map(lambda x:''.join(x), pairwise(str2)))
    
    inter = intersection(comb1, comb2)
    uni = union(comb1, comb2) 
    
    print(not inter, not uni)
    
    if not inter and not uni:
        return 1
    else:
        return int(65536 * (len(inter) / len(uni)))