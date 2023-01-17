def solution(food):
    answer = ''
    for i, f in enumerate(food[1:]):
        if f // 2:
            answer += str(i + 1) * (f // 2)
    return f'{answer}0{"".join((list(reversed(answer))))}'