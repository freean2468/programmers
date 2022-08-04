# https://school.programmers.co.kr/learn/courses/30/lessons/12940
def solution(n, m):
    nd = [d for d in range(1, n+1) if n % d == 0]
    md = [d for d in range(1, m+1) if m % d == 0]
    
    nm = []
    mm = []
    
    max_count = 1
    mini_count = 1
    while True:
        maxi = max(n, m)
        mini = min(n, m)
        maxi *= max_count
        nm.append(maxi)
        max_count += 1
        
        multi = 0
        while multi < maxi:
            multi = mini * mini_count
            mm.append(multi)
            mini_count += 1
        
        lcm_list = [m for m in nm if m in mm]
        
        if len(lcm_list) > 0:
            break    
    
    gcd = max([d for d in nd if d in md])
    lcm = min(lcm_list)
                    
    return [gcd, lcm]