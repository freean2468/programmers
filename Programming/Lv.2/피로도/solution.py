# https://school.programmers.co.kr/learn/courses/30/lessons/87946
def depth(d, k, choosen, rest):
    condition, consumed = choosen
    if k >= condition:
        if rest:
            k -= consumed
            return solution(k, rest, d + 1)
        else:
            return d
    else:
        return d - 1

def solution(k, dungeons, d=1):
    answer = []
    for i, e in enumerate(dungeons):
        answer.append(depth(d, k, e, dungeons[:i] + dungeons[i + 1:]))
    return max(answer)