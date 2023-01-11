# https://school.programmers.co.kr/learn/courses/30/lessons/120880
def solution(numlist, n):
    meta = []
    answer = []

    for i, num in enumerate(numlist):
        meta.append({
            'value': num,
            'diff': abs(n - num),
            'consumed': False,
            'index': i
        })
    
    for num in numlist:
        closest = {
            'value': 100001,
            'diff': 100001,
            'consumed': False
        }
        for i, _ in enumerate(meta):
            if not _['consumed']:
                if _['diff'] < closest['diff']:
                    closest = _
                elif _['diff'] == closest['diff']:
                    closest = _ if _['value'] > closest['value'] else closest
        answer.append(closest['value'])
        meta[closest['index']]['consumed'] = True
            
    return answer