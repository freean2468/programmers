# https://school.programmers.co.kr/learn/courses/30/lessons/76502
class Stack:
    def __init__(self, size):
        self.index = 0
        self.stack = [None] * size
        self.closes = [')', '}', ']']
        self.opens = ['(', '{', '[']
    
    def push(self, e):
        if e in self.closes and self.index > 0:
            if e == ')' and self.stack[self.index - 1] == '(':
                self.index -= 1
                self.stack[self.index] = None
                return
            elif e == '}' and self.stack[self.index - 1] == '{':
                self.index -= 1
                self.stack[self.index] = None
                return
            elif e == ']' and self.stack[self.index - 1] == '[':
                self.index -= 1
                self.stack[self.index] = None
                return
        self.stack[self.index] = e
        self.index += 1
        
    
def solution(s):
    answer = 0
    for i in s:
        stack = Stack(len(s))
        for c in s:
            stack.push(c)
        if not stack.index:
            answer += 1
        s = s[1:] + s[0]
    return answer