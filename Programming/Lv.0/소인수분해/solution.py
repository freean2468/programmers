# https://school.programmers.co.kr/learn/courses/30/lessons/120852
def solution(n):
    primes = [v for v in range(2, n + 1)]
    
    for p in primes:
        multiple = p + p
        while multiple <= primes[-1]:
            if multiple in primes:
                primes.remove(multiple)
            multiple += p
    
    answer = []
    index = 0
    
    while n != 1:
        if n % primes[index] == 0:
            n //= primes[index]
            answer.append(primes[index])
        else:
            index += 1
        
    return sorted(list(set(answer)))
