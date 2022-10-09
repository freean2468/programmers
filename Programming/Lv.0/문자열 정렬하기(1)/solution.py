# https://school.programmers.co.kr/learn/courses/30/lessons/120850
def solution(my_string):
    numeric_list = [str(v) for v in range(0, 10)]
    return sorted(map(int, filter(lambda x: x in numeric_list, list(my_string))))