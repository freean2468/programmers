# https://school.programmers.co.kr/learn/courses/30/lessons/120895
def solution(my_string, num1, num2):
    mutated = list(my_string)
    mutated[num1], mutated[num2] = mutated[num2], mutated[num1]
    return ''.join(list(mutated))
