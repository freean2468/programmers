class Stack:
    def __init__(self):
        self.index = 0
        self.hambergers = 0
        self.list = []

    def push(self, n):
        if len(self.list) == self.index:
            self.list.append(n)
        else:
            self.list[self.index] = n
        self.index += 1
        if self.index > 3 and self.list[self.index - 4:self.index] == [1, 2, 3, 1]:
            self.hambergers += 1
            self.index -= 4
        

def solution(ingredient):
    index = len(ingredient)
    if index < 4:
        return 0
    
    stack = Stack()
    for n in ingredient:
        stack.push(n)
    
    return stack.hambergers