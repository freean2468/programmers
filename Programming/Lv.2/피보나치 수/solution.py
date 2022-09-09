# https://school.programmers.co.kr/learn/courses/30/lessons/12945#
def fibonacci(i):
    if i <= 1:
        return i
    
    arr = [0, 1]
    for n in range(2, i + 1):
        arr.append(arr[n - 2] + arr[n - 1])
        
    return arr.pop()
    

def solution(n):
    return fibonacci(n) % 1234567