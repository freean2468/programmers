# https://school.programmers.co.kr/learn/courses/30/lessons/120863#
def solution(polynomial):
    x_list = []
    number = 0
    
    for ter in filter(lambda x:x != '+', polynomial.split(' ')):
        if 'x' in ter:
            ter = ter.replace('x', '')
            if ter == '':
                x_list.append(1)
            else:
                x_list.append(int(ter))
        else:
            number += int(ter)
    
    x_sum = sum(x_list)
    
    if x_sum:
        if x_sum == 1:
            return 'x + ' + str(number) if number else 'x'
        else:
            return str(x_sum) + 'x + ' + str(number) if number else str(x_sum) + 'x'
    else:
        return str(number) if number else ''
