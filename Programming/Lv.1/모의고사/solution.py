# https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3
def solution(answers):
    f = [1,2,3,4,5]
    s = [2,1,2,3,2,4,2,5]
    t = [3,3,1,1,2,2,4,4,5,5]
    correct = [0, 0, 0]
    
    for i, a in enumerate(answers):
        if f[i % len(f)] == a:
            correct[0] += 1
        if s[i % len(s)] == a:
            correct[1] += 1
        if t[i % len(t)] == a:
            correct[2] += 1
        
    m = max(correct)
    
    return [i + 1 for i, c in enumerate(correct) if c == m]