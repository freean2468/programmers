# https://school.programmers.co.kr/learn/courses/30/lessons/42626#
class Heap:
    def __init__(self, l):
        self.h = l
        self.i = 0
        
    def length(self):
        return len(self.h) - self.i
    
    def is_end(self):
        return True if len(self.h) - self.i == 1 else False
    
    def is_empty(self):
        return True if len(self.h) - self.i == 0 else False
    
    def fulfill_scoville(self):
        return True if self.is_empty() or self[0] >= self.k else False
    
    def append(self, e):
        self.h.append(e)
        
    def shift(self):
        t = self.h[self.i]
        self.i += 1
        return t
    
    def __getitem__(self, i):
        return self.h[self.i + i]
    
    
def solution(scoville, K):
    answer = 0
    Heap.k = K
    scoville_heap = Heap(sorted(scoville))
    scrambled_heap = Heap([])
    
    while scoville_heap.fulfill_scoville() == False or scrambled_heap.fulfill_scoville() == False:
        shifted = []
        for i in range(2):
            if scoville_heap.is_empty() == True and scrambled_heap.is_empty() == True:
                return -1
            elif scoville_heap.is_empty() == False and scrambled_heap.is_empty() == False:
                if scoville_heap[0] < scrambled_heap[0]:
                    shifted.append(scoville_heap.shift())
                else:
                    shifted.append(scrambled_heap.shift())
            elif scoville_heap.is_empty():
                shifted.append(scrambled_heap.shift())
            elif scrambled_heap.is_empty():
                shifted.append(scoville_heap.shift())

        scrambled_heap.append(shifted[0] + shifted[1] * 2)
        answer += 1
    
    if scoville_heap.length() > 0:
        if scoville_heap[0] < K:
            return -1
    
    if scrambled_heap.length() > 0:
        if scrambled_heap[0] < K:
            return -1
    
    return answer