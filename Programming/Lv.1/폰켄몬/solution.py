# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3
def solution(nums):
    return min(len(set(nums)), int(len(nums) / 2))