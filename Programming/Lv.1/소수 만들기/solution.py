# https://school.programmers.co.kr/learn/courses/30/lessons/12977?language=python3
import math

def solution(nums):
    answer = 0

    for i, n in enumerate(nums):
        nums2 = nums[i + 1:]
        for j, n2 in enumerate(nums2):
            nums3 = nums2[j + 1:]
            for k, n3 in enumerate(nums3):
                t = n + n2 + n3
                is_prime = True
                for l in range(2, int(t / 2)):
                    if t % l == 0:
                        is_prime = False
                        break
                        
                answer += (1 if is_prime else 0)
                    

    return answer