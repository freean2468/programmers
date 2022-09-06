from collections import deque    

def solution(maps):
    def move(x, y):
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        queue = deque()
        queue.append((y, x))

        while queue:
            y, x = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if nx < 0 or nx >= len(maps[0]) or ny < 0 or ny >= len(maps):
                    continue

                if maps[ny][nx] == 0:
                    continue

                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    queue.append((ny, nx))

        return maps[len(maps) - 1][len(maps[0]) - 1] 
        
    answer = move(0, 0)
    return -1 if answer == 1 else answer
