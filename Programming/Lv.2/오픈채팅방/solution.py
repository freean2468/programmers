# https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    db = {}
    for r in record:
        split = r.split(' ')
        if split[0] != "Leave":
            db[split[1]] = split[2]
        
    for r in record:
        split = r.split(' ')
        if split[0] == "Enter":
            answer.append('%s님이 들어왔습니다.' % db[split[1]])
        elif split[0] == "Leave":
            answer.append('%s님이 나갔습니다.' % db[split[1]])
    
    return answer