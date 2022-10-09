# https://school.programmers.co.kr/learn/courses/30/lessons/120834
def solution(age):
    return ''.join(list(map(lambda x:chr(ord('a') + int(x)), list(str(age)))))
