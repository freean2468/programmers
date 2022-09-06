# https://school.programmers.co.kr/learn/courses/30/lessons/72411?language=python3
from itertools import combinations

def solution(orders, course):
    answer = []
    db = {}
    len_db = {}
    
    for o in orders:
        o = ''.join(sorted(o))
        for length in course:
            for l in list(combinations(o, length)):
                m = ''.join(l)
                
                if m in db:
                    db[m] += 1
                    if length in len_db:
                        for t in len_db[length]:
                            if t[1] < db[m]:
                                len_db[length] = [(m, db[m])]
                                break
                            elif t[1] == db[m]:
                                len_db[length].append((m, db[m]))
                                break
                    else:
                        len_db[length] = [(m, db[m])]
                else:
                    db[m] = 1       
        
    for k, v in len_db.items():
        for l in v:
            answer.append(l[0])
    
    return sorted(answer)

# collections.Counter.most_common을 사용하면 편하다...
# import collections
# import itertools

# def solution(orders, course):
#     result = []

#     for course_size in course:
#         order_combinations = []
#         for order in orders:
#             order_combinations += itertools.combinations(sorted(order), course_size)

#         most_ordered = collections.Counter(order_combinations).most_common()
#         result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

#     return [ ''.join(v) for v in sorted(result) ]