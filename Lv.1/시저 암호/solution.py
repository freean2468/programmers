# https://school.programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    lower = [chr(l) for l in range(ord('a'), ord('z') + 1)]
    upper = [chr(u) for u in range(ord('A'), ord('Z') + 1)]
    answer = []
    
    for c in s:
        if c in lower:
            answer.append(lower[(lower.index(c) + n) % len(lower)])
        elif c in upper:
            answer.append(upper[(upper.index(c) + n) % len(upper)])
        else:
            answer.append(' ')
        
    return ''.join(answer)