# https://school.programmers.co.kr/learn/courses/30/lessons/12909
class Stack():
    def __init__(self):
        self.s = []
        
    def push(self, item):
        if self.s and item == ')' and self.s[-1] == '(':
            self.s.pop()
        else:
            self.s.append(item)
            
    def is_empty(self):
        return True if not self.s else False

        
def solution(s):
    stack = Stack()
    
    for p in s:
        stack.push(p)
    
    return stack.is_empty()