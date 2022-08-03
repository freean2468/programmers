# https://school.programmers.co.kr/learn/courses/30/lessons/64061?language=python3
def solution(board, moves):
    answer = 0
    queue = []
    
    for m in moves:
        for b in board:
            if b[m - 1] > 0:
                queue.append(b[m - 1])
                length = len(queue)
                
                if length >= 2 and queue[length - 1] == queue[length - 2]:
                    queue = queue[:length - 2]
                    answer += 2
                
                b[m - 1] = 0
                break
                
    return answer