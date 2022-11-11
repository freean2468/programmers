# https://school.programmers.co.kr/learn/courses/30/lessons/120861
def solution(keyinput, board):
    width = board[0] // 2
    height = board[1] // 2
    answer = [0, 0]
    key_set = {
        "left":[-1, 0],
        "right":[1, 0],
        "up":[0, 1],
        "down":[0, -1]
    }
    
    for key in keyinput:
        x, y = key_set[key][0] + answer[0], key_set[key][1] + answer[1]
        x = max(-width, x)
        x = min(width, x)
        y = max(-height, y)
        y = min(height, y)
        answer = [x, y]
        
    return answer
