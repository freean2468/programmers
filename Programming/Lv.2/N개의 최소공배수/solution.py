# https://school.programmers.co.kr/learn/courses/30/lessons/12953#
def solution(arr):
    answer = 1
    divisor = 2
    
    while len(list(filter(lambda x:x != 1, arr))):
        flag = False
        for i, n in enumerate(arr):
            if n % divisor == 0:
                arr[i] = n / divisor
                flag = True
        
        if flag:
            answer *= divisor
        else:
            divisor += 1
        
    return answer