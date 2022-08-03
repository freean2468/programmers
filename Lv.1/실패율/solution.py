# https://school.programmers.co.kr/learn/courses/30/lessons/42889?language=python3
def solution(N, stages):
    length = len(stages)
    stages.sort()
    stages_info = {}
    count = 0
    n = 1
    
    for i, s in enumerate(stages):
        while(n < s):
            stages_info[n] = {
                "count": count,
                "fail_rate": count / (length - sum([v["count"] for k, v in stages_info.items() if k < n]))
            }
            n += 1
            count = 0

        if i + 1 < length and s != stages[i + 1]:
            count += 1
            stages_info[n] = {
                "count": count,
                "fail_rate": count / (length - sum([v["count"] for k, v in stages_info.items() if k < n]))
            }
            count = 0;
            n += 1
        elif i + 1 == length:
            count += 1
            de = length - sum([v["count"] for k, v in stages_info.items() if k < n])
            if de == 0:
                  de = count
                  
            stages_info[n] = {
                "count": count,
                "fail_rate": count / de
            }
        else:
            count += 1;
    
    answer = [[k, v["fail_rate"]] for k, v in stages_info.items()]
    while len(answer) <= N:
        answer.append([len(answer) + 1, 0])
    answer = answer[:N]
    
    answer.sort(key=lambda x: x[1], reverse=True)
    
    return [v[0] for v in answer]