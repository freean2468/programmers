from collections import Counter
from functools import reduce

def solution(clothes):
    count = Counter([cloth_kind for cloth_name, cloth_kind in clothes])
    return reduce(lambda x, y:x*(y+1), count.values(), 1) - 1