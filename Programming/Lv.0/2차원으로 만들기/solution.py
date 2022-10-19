# https://school.programmers.co.kr/learn/courses/30/lessons/120842
def solution(num_list, n):
    return [num_list[n*(v - 1):n*v] for v in range(1, len(num_list)//n + 1)]
