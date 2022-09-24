# https://school.programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    index = 0
    rindex = len(people) - 1
    
    while index <= rindex:
        rest = limit - people[index]
        if index + 1 < len(people) and rest >= people[rindex]:
            index += 1
            rindex -= 1
        else:
            index += 1
        
        answer += 1
        
    return answer