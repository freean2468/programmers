# https://school.programmers.co.kr/learn/courses/30/lessons/12921#
prime_table = [2]
    
def solution(n):
    prime_count = 1
    for v in range(3, n + 1):
        is_prime = True
        
        if v % 2 == 1:
            sqrt = v ** 0.5
            if sqrt.is_integer():
                continue
                
            for p in prime_table:
                if p > sqrt:
                    break
                    
                if v % p == 0:
                    is_prime = False
                    break

            if is_prime == True:
                prime_table.append(v)
                prime_count += 1
            
    return prime_count