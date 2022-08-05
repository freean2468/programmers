# https://school.programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []
    
    while len(progresses) > 0:
        done = 0
        
        while len(progresses) > 0 and progresses[0] >= 100:
            progresses = progresses[1:]
            speeds = speeds[1:]
            done += 1
        
        if done > 0:
            answer.append(done)
            
        progresses = [p + s for p, s in zip(progresses, speeds)]
    
    return answer