# https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
# 겨우 통과. DFS를 이진 트리마냥 접근.
class Node:
    def __init__(self, n):
        self.n = n
        self.l = None
        self.r = None
        
    def add(self, n):
        if self.l:
            self.l.add(n)
            self.r.add(n)
        else:
            self.l = Node(n)
            self.r = Node(-n)
            
    def comb(self):
        if self.l:
            return [[self.n + lv1, self.n + rv1] for lv, rv in zip(self.l.comb(), self.r.comb()) for lv1, rv1 in zip(lv, rv)]
        else:
            return [[self.n]]

def solution(numbers, target):
    answer = 0
        
    r = Node(0)
    Node.t = target
    Node.a = 0
    
    for n in numbers:
        r.add(n)
        
    for cand in r.comb():
        for v in cand:
            if v == target:
                answer += 1
        
    return answer

# target을 줄여나가며 재귀 함수를 두 가지 경우의 수로 계속 실행해가며 최종 조건을 만족하면 갯수 카운팅 방식
# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# itertools -> product 활용
# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)

# DFS 정석 풀이
# answer = 0
# def DFS(idx, numbers, target, value):
#     global answer
#     N = len(numbers)
#     if(idx== N and target == value):
#         answer += 1
#         return
#     if(idx == N):
#         return

#     DFS(idx+1,numbers,target,value+numbers[idx])
#     DFS(idx+1,numbers,target,value-numbers[idx])
# def solution(numbers, target):
#     global answer
#     DFS(0,numbers,target,0)
#     return answer