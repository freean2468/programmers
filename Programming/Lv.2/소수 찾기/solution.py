# https://school.programmers.co.kr/learn/courses/30/lessons/42839
def permu(arr):
    if len(arr) == 1:
        return arr
    
    agg = []
    
    for i, c in enumerate(arr):
        agg.append(c)
        for c2 in permu(arr[:i] + arr[i+1:]):
            agg.append(c + c2)
            
    return agg
    

def solution(numbers):
    answer = 0
    ap = set([int(s) for s in permu(numbers)])
    
    for n in ap:
        flag = False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                flag = True
                break
                
        if n >= 2 and flag is False:
            answer += 1
                
    return answer
    