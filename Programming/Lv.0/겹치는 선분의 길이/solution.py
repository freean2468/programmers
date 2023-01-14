# https://school.programmers.co.kr/learn/courses/30/lessons/120876
answer = []

def add_line(line):
    lx1, lx2 = line
    for i, _ in enumerate(answer):
        x1, x2 = _
        if x2 > lx1:
            if x2 > lx2:
                return
            else:
                answer[i][1] = lx2
                return
    
    answer.append(line)
                

def solution(lines):
    lines.sort()
    for i, line in enumerate(lines[:-1]):
        x1, x2 = line
        for j in range(i+1, len(line) + 1):
            nx1, nx2 = lines[j]
            if x2 > nx1:
                if nx2 > x2:
                    add_line([nx1, x2])
                else:
                    add_line([nx1, nx2])
    return sum([_[1] - _[0] for _ in answer])
