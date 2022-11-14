# https://school.programmers.co.kr/learn/courses/30/lessons/120866
def solution(board):
    n = len(board) - 1
    co_set = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]
    for i, r in enumerate(board):
        for j, c in enumerate(r):
            if c == 1:
                for dx, dy in co_set:
                    x = min(n, i+dx)
                    x = max(0, x)
                    y = min(n, j+dy)
                    y = max(0, y)
                    
                    if board[x][y] == 0:
                        board[x][y] = 2
                        
    answer = 0
    
    for r in board:
        for c in r:
            if c == 0:
                answer += 1
    
    return answer
