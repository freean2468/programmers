# https://school.programmers.co.kr/learn/courses/30/lessons/120882
def solution(score):
    score = [s[0] + s[1] for s in score]
    rank = 1
    ranks = []
    for s in score:
        for s1 in score:
            if s1 > s:
                rank += 1
        ranks.append(rank)
        rank = 1
    return ranks