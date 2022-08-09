from itertools import permutations
import re
from copy import deepcopy
import operator

def solution(expression):
    answer = []
    op_lookup = {'*': operator.mul, '+': operator.add, '-': operator.sub}
    operators = ['*', '+', '-']
    op_orders = list(permutations(operators, 3))
    numbers = list(map(lambda x: int(x), re.findall('\d{1,3}', expression)))
    operators = re.findall('\-|\*|\+', expression)
    
    for orders in op_orders:
        n_cp = deepcopy(numbers)
        op_cp = deepcopy(operators)
        for op in orders:
            try:
                while op_cp.index(op) >= 0:
                    i = op_cp.index(op)
                    n_cp[i] = op_lookup[op](n_cp[i], n_cp[i+1])
                    del n_cp[i+1]
                    del op_cp[i]
            except ValueError:
                pass
                
        answer.append(abs(n_cp[0]))
    
    return max(answer)