# https://school.programmers.co.kr/learn/courses/30/lessons/86052
#    to right   to down     to left     to up
d = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
cycle = []

def get_in(p, c):
    if p == 'L':
        c = c - 1 if c - 1 >= 0 else len(d) - 1
    elif p == 'R':
        c = (c + 1) % len(d)

    return c
            
def go_cycle(depth, y, x, direction):
    global cycle
    
    if depth == 0:
        cycle = []
    elif depth > max_try:
        return 0
    
    if depth > 0:
        cy, cx, cout = cycle[0]
        if cx == x and cy == y and cout == direction:
            print(cycle, y, x, direction)
            return len(cycle)
    
    c = (y, x, direction)
    cycle.append(c)

    nx = (x + d[direction][1]) % max_x
    if nx < 0:
        nx = max_x - 1

    ny = (y + d[direction][0]) % max_y
    if ny < 0:
        ny = max_y - 1

    return go_cycle(depth + 1, ny, nx, get_in(m[ny][nx], direction))

def solution(grid):
    answer = []
    global m
    global max_try
    global max_x
    global max_y
    
    m = [[c for c in r] for r in grid]
    max_x = len(m[0])
    max_y = len(m)
    max_try = (max_x * max_y) ** 2
    
    for i, c in enumerate(m):
        for j, n in enumerate(c):
            if i == 0:
                answer.append(go_cycle(0, i, j, 1))
            if i == len(m) - 1:
                answer.append(go_cycle(0, i, j, 3))
            if j == 0:
                answer.append(go_cycle(0, i, j, 0))
            if j == len(c) - 1:
                answer.append(go_cycle(0, i, j, 2))
                
    return sorted(list(filter(lambda x: x > 0, answer)))