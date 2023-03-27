# https://school.programmers.co.kr/learn/courses/30/lessons/92335
def convert_base(n, k):
    result = ""
    while n > 0:
        n, remainder = divmod(n, k)
        result = str(remainder) + result
    return result


def is_prime(number):
    for cand in range(2, int(number ** 0.5) + 1):
            if number % cand == 0:
                return False
    return True
    

def solution(n, k):
    k_base = convert_base(n, k)
    split = k_base.split('0')
    ten_base = [int(s) for s in split if s != '1' and s != '']
    answer = 0
    for number in ten_base:
        if is_prime(number):
            answer += 1
    return answer