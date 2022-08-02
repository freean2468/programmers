# https://school.programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    left = [1, 4, 7, '*']
    right = [3, 6, 9, '#']
    middle = [2, 5, 8, 0]
    
    lh = [0, 3]
    rh = [2, 3]
    
    answer = []
    
    for n in numbers:
        if n in left:
            lh = [0, left.index(n)]
            answer.append("L")
        elif n in right:
            rh = [2, right.index(n)]
            answer.append("R")
        else:
            ni = middle.index(n)
            
            if (lh[0] == 0 and rh[0] == 2) or (lh[0] == 1 and rh[0] == 1):
                ld = abs(ni - lh[1])
                rd = abs(ni - rh[1])
            elif rh[0] == 1:
                ld = abs(ni - lh[1]) + 1
                rd = abs(ni - rh[1])
            else:
                ld = abs(ni - lh[1])
                rd = abs(ni - rh[1]) + 1
            
            if ld == rd:
                if hand == "right":
                    rh = [1, ni]
                    answer.append("R")
                else:
                    lh = [1, ni]
                    answer.append("L")
            elif ld < rd:
                lh = [1, ni]
                answer.append("L")
            else:
                rh = [1, ni]
                answer.append("R")
                
    return ''.join(answer)
                
                
