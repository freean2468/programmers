# https://school.programmers.co.kr/learn/courses/30/lessons/81302#
global p

def dfs(d, ori, oci, ri, ci):
    global p
    print(p)
    rooms = list(filter(lambda x: (x[0] > -1 and x[1] > -1) and not (x[0] == ori and x[1] == oci) , [(ri, ci - 1), (ri, ci + 1), (ri + 1, ci), (ri - 1, ci)]))
    answer = []
    
    for r in rooms:
        try:
            # print(r, r[0], r[1], p, p[r[0]], p[r[0]][r[1]])
            rv = p[r[0]][r[1]]
            if rv == 'P':
                return 0
            
            if d == 1 and rv == 'O':
                answer.append(dfs(d + 1, ori, oci, r[0], r[1]))
        except IndexError:
            pass

    if d == 2:
        return 1
    else:
        if 0 in answer:
            return 0
        else:
            return 1
        
    
def loop_c(ri, rv):
    global p
    
    for ci, cv in enumerate(rv):
        if cv == 'P' and dfs(1, ri, ci, ri, ci) == 0:
            return 0
            
    return 1
            
def loop_r(p):
    for ri, rv in enumerate(p):
        if loop_c(ri, rv) == 0:
            return 0
        
    return 1

def solution(places):
    global p
    p = places
    answer = []
    
    for p in places:
        answer.append(loop_r(p))
        
    return answer