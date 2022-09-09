# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def decimal_to_binary(num):
    quotient = num // 2
    remainder = num % 2
    
    if num > 1:
        return str(remainder) + decimal_to_binary(quotient)
    else:
        return str(num)
    

def binary_conversion(bi, d):
    filtered = list(filter(lambda x:x == '1', bi))
    zero_count = len(bi) - len(filtered)
    
    if (len(filtered) == 1 and filtered[0] == "1"):
        return (d, zero_count)
    else:
        res = binary_conversion(decimal_to_binary(len(filtered)), d + 1)
        return (res[0], res[1] + zero_count)
    

def solution(s):
    answer = binary_conversion(s, 1)
    return [answer[0], answer[1]]