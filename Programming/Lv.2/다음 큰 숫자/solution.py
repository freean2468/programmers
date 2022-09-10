# https://school.programmers.co.kr/learn/courses/30/lessons/12911#
def solution(n):
    splitted = [v for v in str(bin(n)[2:])]
    sliced = []
    
    if len(list(filter(lambda x:x == '0', splitted))) == 0:
        splitted.insert(0, '1')
        sliced = splitted
        sliced[1] = '0'
    else:
        splitted_reversed = list(reversed(splitted))
        flag = False
        
        for i, v in enumerate(splitted_reversed):
            sliced.append(v)

            if i > 0 and sliced[i] == '0' and sliced[i-1] == '1' and not flag:
                sliced[i], sliced[i - 1] = sliced[i - 1], sliced[i]
                
                if i >= 2:
                    one_count = len(list(filter(lambda x:x == '1', sliced[:i-1])))
                    
                    for j in range(one_count):
                        sliced[j] = '1'
                    for j in range(one_count, i - 1):
                        sliced[j] = '0'
                
                flag = True
                
        if not flag:
            splitted.insert(0, '1')
            sliced = splitted
            sliced[1] = '0'
            t = []
            if len(sliced) >= 2:
                zero_count = len(list(filter(lambda x: x == '0', sliced[2:])))
                one_count = len(sliced[2:]) - zero_count
                for j in range(zero_count):
                    t.append('0')
                for j in range(one_count):
                    t.append('1')
            sliced = sliced[:2] + t
        else:    
            sliced.reverse()
                
    next_big = ''.join(sliced)
    
    return int(next_big, 2)
