# https://school.programmers.co.kr/learn/courses/30/lessons/136798
def solution(number, limit, power):
    sieve = ['*'] * number
    sieve[0] = False
    for i in range(2, number + 1):
        for n in range(i, number + 1, i):
            index = n - 1
            if i == n and sieve[index] == '*':
                sieve[index] = True
            elif sieve[index] == '*':
                sieve[index] = False
    
    primes = [i + 1 for i, v in enumerate(sieve) if v == True]
        
    divisor_counts = []
    answer = 0
    for n in range(1, number + 1): 
        factor_counts = []
            
        for i, p in enumerate(primes):
            factor_count = 0
            while n % p == 0:                    
                n //= p
                factor_count += 1
            if factor_count > 0:
                factor_counts.append(factor_count + 1)
            if n == 1:
                break
        base = 1
        for c in factor_counts:
            base *= c
        if base > limit:
            answer += power
        else:
            answer += base
    
    return answer