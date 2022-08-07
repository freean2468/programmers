# https://school.programmers.co.kr/learn/courses/30/lessons/60058
class Stack:
    def __init__(self):
        self.s = []
        
    def push(self, b):
        self.s.append(b)
        
        slen = len(self.s)
        if slen > 1 and self.s[slen - 1] == ')' and self.s[slen - 2] == '(':
            self.s.pop()
            self.s.pop()        
        
    def is_empty(self):
        if self.s:
            return False
        else:
            return True

def solution(p):
    if p == '':
        return ''
    
    oc = 0
    cc = 0
    u = ''
    v = ''
    
    for i, c in enumerate(p):
        if c == '(':
            oc += 1
        elif c == ')':
            cc += 1
            
        if oc == cc:
            u = p[:i+1]
            v = p[i+1:]
            break
            
    s = Stack()
    for c in u:
        s.push(c)
            
    if s.is_empty():
        return u + solution(v)
    else:
        e = '(' + solution(v) + ')'
        
        if u:
            u = list(u)[1:]
            u.pop()
        else:
            u = []
        
        for i, c in enumerate(u):
            if c == ')':
                u[i] = '('
            elif c == '(':
                u[i] = ')'
                
        u = ''.join(u)
                
        return e + u

# pythonic한 방법
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
