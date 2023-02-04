# https://school.programmers.co.kr/learn/courses/30/lessons/42747#
def solution(citations):
    h = 0
    for i in range(max(citations) + 1):
        upper = []
        under = []
        for c in citations:
            if c < i:
                under.append(c)
            else:
                upper.append(c)
        if len(upper) >= i and len(under) <= i:
            h = i
    return h