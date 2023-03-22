from collections import Counter

def solution(k, tangerine):
    counter = {}
    for key, v in Counter(tangerine).items():
        if v in counter:
            counter[v].append(key)
        else:
            counter[v] = [key]
    size_count = 0
    for key in reversed(sorted(counter.keys())):
        for _ in counter[key]:
            k -= key
            size_count += 1
            if k < 1:
                return size_count
