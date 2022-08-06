# https://school.programmers.co.kr/learn/courses/30/lessons/77485
# 무식하게 직접 다 돌리려다가 이건 가독성, 유지보수성이 너무 떨어져서 다른 방안을 모색함.
def solution(rows, columns, queries):
    answer = [[j + 1 + i*rows for j in range(columns)] for i in range(rows)]
    mins = []
    
    print(answer)
    
    for q in queries:
        y1 = q[0]
        x1 = q[1]
        y2 = q[2]
        x2 = q[3]
        
        tl = []
        tl.append(answer[y1 - 1][x2 - 1])
        t = tl[-1]
        
        for i in reversed(range(x1, x2)):
            tl.append(answer[y1 - 1][i - 1])
            answer[y1 - 1][i] = tl[-1]
        
        print(answer)
        
        tl.append(answer[y2 - 1][x2 - 1])
        t2 = tl[-1]
        
        for i in reversed(range(y1 + 1, y2)):
            tl.append(answer[i - 1][x2 - 1])
            answer[i][x2 - 1] = tl[-1]
            
        answer[y1][x2 - 1] = t
        tl.append(answer[y2 - 1][x2 - 2])
        t = tl[-1]
        
        for i in range(x1, x2 - 2):
            tl.append(answer[y2 - 1][i + 1])
            answer[y2 - 1][i] = tl[-1]
        
        answer[y2 - 1][x2 - 2] = t2
        tl.append(answer[y2 - 1][x1 - 1])
        t2 = tl[-1]
        answer[y2 - 1][x1 - 1] = t
        
        for i in range(y1 - 1, y2 - 1):
            tl.append(answer[i + 1][x1 - 1])
            answer[i][x1 - 1] = tl [-1]
            
        answer[y2 - 2][x1 - 1] = t2
        
        mins.append(min(tl))
        
        print(answer)
    
    return mins