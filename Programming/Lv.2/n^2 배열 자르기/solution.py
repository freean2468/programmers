def solution(n, left, right):
    answer = []
    for index in range(left, right + 1):
        i = index % n
        j = index // n
        answer.append(i + 1 if j < i else j + 1)
    return answer