# https://school.programmers.co.kr/learn/courses/30/lessons/77485#
# 선형큐 아이디어를 접목해 풀이
class Queue:
    def __init__(self):
        self.q = []
        self.i = -1
        
    def push(self, n):
        self.q.append(n)
        
    def shift(self):
        v = self.q[self.i]
        self.i = (self.i + 1) % len(self.q)
        return v
    
    def mini(self):
        return min(self.q)
    
    def print(self):
        print(self.q)

def solution(rows, columns, queries):
    lists = [[j + 1 + i*columns for j in range(columns)] for i in range(rows)]
    
    answer = []
    
    for q in queries:
        y1, x1, y2, x2 = q
        queue = Queue()
        
        for i in range(x1 - 1, x2):
            queue.push(lists[y1-1][i])
            
        for i in range(y1, y2):
            queue.push(lists[i][x2 - 1])

        for i in reversed(range(x1 - 1, x2 - 1)):
            queue.push(lists[y2-1][i])
            
        for i in reversed(range(y1, y2 - 1)):
            queue.push(lists[i][x1 - 1])
        
        for i in range(x1 - 1, x2):
            lists[y1-1][i] = queue.shift()
            
        for i in range(y1, y2):
            lists[i][x2 - 1] = queue.shift()

        for i in reversed(range(x1 - 1, x2 - 1)):
            lists[y2-1][i] = queue.shift()
            
        for i in reversed(range(y1, y2 - 1)):
            lists[i][x1 - 1] = queue.shift()
            
        answer.append(queue.mini())
        
    return answer