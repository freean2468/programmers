# https://school.programmers.co.kr/learn/courses/30/lessons/133499
def is_impossible(impossible, b):
    for im in impossible:
        if im in b:
            return True
    return False

def solution(babbling):
    words = ['aya', 'ye', 'woo', 'ma']
    impossible = [w * 2 for w in words]
    answer = 0
    for b in babbling:
        if is_impossible(impossible, b):
            continue
        for w in words:
            b = b.replace(w, '*')
        b = b.replace('*', '')
        if b == '':
            answer += 1
    return answer