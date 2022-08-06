# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 정규표현식 접근, 시간 초과
import re

def solution(s):
    cc = [chr(c)+chr(c) for c in range(ord('a'), ord('z') + 1)]
    
    while True:
        ps = s
        s = re.sub(r'%s' % '|'.join(cc), '', s)
        if ps == s:
            return 0
        elif s == '':
            return 1

# 35.3 / 100.0
# import re

# def solution(s):
#     cc = [chr(c)+chr(c) for c in range(ord('a'), ord('z') + 1)]
#     regex = '|'.join(cc)
    
#     while True:
#         m = re.search(regex, s)
#         if m != None:
#             m = m.group()
#             s = s.replace(m, '')
#         else:
#             if len(s) > 0:
#                 return 0
#             else:
#                 return 1

# 35.3 / 100.0
# def solution(s):
#     while True:
#         m = ''
#         for i, v in enumerate(s):
#             if i < len(s) - 1 and v == s[i + 1]:
#                 m = v * 2
#                 break
        
#         if m != '':
#             s = ''.join(s.split(m))
#         else:
#             if len(s) > 0:
#                 return 0
#             else:
#                 return 1

# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 스택을 이용한 접근법.
class Stack():
    def __init__(self):
        self.l = []
        self.i = -1
        
    def push(self, e):
        self.l.append(e)
        self.i += 1
        
        while True:
            if self.i >= 1 and self.l[self.i] == self.l[self.i-1]:
                self.l.pop()
                self.l.pop()
                self.i -= 2
            else:
                break
    
def solution(s):
    stack = Stack()
    
    for c in s:
        stack.push(c)
    
    if stack.i == -1:
        return 1
    else:
        return 0