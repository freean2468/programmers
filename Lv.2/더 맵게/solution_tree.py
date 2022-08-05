# https://school.programmers.co.kr/learn/courses/30/lessons/42626#
# 이진 트리 접근법 => 57.1
class Node:
    def __init__(self, n):
        self.left = None
        self.right = None
        self.n = n
        self.count = 1
        
    def print(self):
        if self.left != None:
            self.left.print()
            
        if self.n != self.k:
            print([self.n, self.count])
        elif self.n == self.k and self.count > 2:
            print([self.n, self.count - 1])
            
        if self.right != None:
            self.right.print()
        
    def insert(self, n):
        if self.n == n:
            self.count += 1
        elif self.n > n:
            if self.left:
                self.left.insert(n)
            else:
                self.left = Node(n)
        elif self.n < n:
            if self.right:
                self.right.insert(n)
            else:
                self.right = Node(n)
                
                
    def pop_left(self, parent):
        if self.left:
            return self.left.pop_left(self)
        else:
            if parent == None:
                # root
                if self.count > 2:
                    self.count -= 1
                    n = self.n
                    return n
                else:
                    # print(1)
                    return self.right.pop_left(self)
            else:
                self.count -= 1
                n = self.n
                if self.count == 0:
                    if parent.left == self:
                        if self.right:
                            parent.left = self.right
                            self.right = None
                        else:
                            parent.left = None
                    elif parent.right == self:
                        if self.left:
                            parent.right = self.left
                            self.left = None
                        else:
                            parent.right = None
                        
                return n
            
    def is_there_left(self):
        return True if self.left else False
    
    def total_count(self):
        t = self.count
        
        if t == self.k:
            self.count -= 1
        
        if self.left:
            t += self.left.total_count()
        
        if self.right:
            t += self.right.total_count()
        
        return t
    
    
def solution(scoville, K):
    answer = 0
    Node.k = K
    root = Node(K)
    
    for s in scoville:
        root.insert(s)
        
    while True:
        if root.total_count() == 1:
            if root.is_there_left() == False:
                answer = -1
            
            break
        elif root.is_there_left() == False:
            break
                
        min1 = root.pop_left(None)
        min2 = root.pop_left(None)

        root.insert(min1 + min2 * 2)
        answer += 1
        # print(answer, min1 + min2 * 2)
        # root.print()
    
    return answer