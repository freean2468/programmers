# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    answer = ''
    data = {
        'RT': 0,
        'CF': 0,
        'JM': 0,
        'AN': 0
    }
    for s, c in zip(survey, choices):
        c -= 4
        if s == 'RT' or s == 'TR':
            if s == 'TR':
                c *= -1
                s = 'RT'
        elif s == 'CF' or s == 'FC':
            if s == 'FC':
                c *= -1
                s = 'CF'
        elif s == 'JM' or s == 'MJ':
            if s == 'MJ':
                c *= -1
                s = 'JM'
        else:
            if s == 'NA':
                c *= -1
                s = 'AN'
        data[s] += c
        
    for k, v in data.items():
        if k == 'RT':
            if v < 1:
                answer += 'R'
            else:
                answer += 'T'
        elif k == 'CF':
            if v < 1:
                answer += 'C'
            else:
                answer += 'F'
        elif k == 'JM':
            if v < 1:
                answer += 'J'
            else:
                answer += 'M'
        else:
            if v < 1:
                answer += 'A'
            else:
                answer += 'N'
            
    return answer