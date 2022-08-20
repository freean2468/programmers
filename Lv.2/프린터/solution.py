# https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    answer = 0
    
    while len(priorities) > 1:
        first = priorities[0]
        
        if first < max(priorities):
            priorities.append(first)
        else:
            answer+=1
            if location == 0:
                return answer
            
        priorities = priorities[1:]
        location -= 1
        if location < 0:
            location = len(priorities) - 1
            
    return answer + 1