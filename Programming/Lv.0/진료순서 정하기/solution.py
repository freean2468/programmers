# https://school.programmers.co.kr/learn/courses/30/lessons/120835
def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    return [sorted_emergency.index(v) + 1 for v in emergency]
