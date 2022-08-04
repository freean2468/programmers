# https://school.programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer = []
    for step in range(1, len(s) // 2 + 1):
        compressed = []
        
        count = 0
        prev_chunk = None
        
        for i in range(0, len(s) + 1, step):
            chunk = s[i:i+step]
            
            if prev_chunk != None and prev_chunk != chunk:
                if count == 1:
                    compressed.append("%s" % (prev_chunk))    
                else:
                    compressed.append("%d%s" % (count, prev_chunk))
                count = 0
            
            count += 1
                
            prev_chunk = chunk
            
        if len(chunk) != step and prev_chunk != "":
            compressed.append("%s" % (prev_chunk))    
            
        answer.append(len(''.join(compressed)))
        
    return min(answer) if len(s) > 1 else 1