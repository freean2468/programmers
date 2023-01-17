def solution(t, p):
    answer = 0
    p_len = len(p)
    for i, _ in enumerate(list(t)):
        if i + p_len <= len(t):
            sub = t[i:i + p_len] 
            if int(sub) <= int(p):
                answer += 1
    return answer