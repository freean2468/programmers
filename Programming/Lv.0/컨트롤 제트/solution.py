# https://school.programmers.co.kr/learn/courses/30/lessons/120853#
def solution(s):
    answer = 0
    prev_list = []
    
    for v in s.split(' '):
        if v != 'Z':
            prev_list.append(int(v))
            answer += prev_list[-1]
        else:
            if prev_list:
                answer -= prev_list.pop()
            
    return answer
