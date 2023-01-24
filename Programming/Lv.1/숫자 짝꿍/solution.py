# https://school.programmers.co.kr/learn/courses/30/lessons/131128
def get_next(n_dict, n, i):
    j = i - 1
    if j < 0:
        return -1
    while True:
        if n_dict[j][n] != -1:
            return j
        elif j > 0:
            j -= 1
        else:
            return -1
    

def solution(X, Y):
    X = list(reversed(sorted(list(X))))
    Y = list(reversed(sorted(list(Y))))
    answer = []
    n_dict = {}
    for i in range(9, -1, -1):
        str_i = str(i)
        n_dict[i] = {
            'x': X.index(str_i) if str_i in X else -1,
            'y': Y.index(str_i) if str_i in Y else -1
        }
    i = 9
    while True:
        xi = n_dict[i]['x']
        yi = n_dict[i]['y']
        if xi != -1 and yi != -1:
            nx = get_next(n_dict, 'x', i)
            ny = get_next(n_dict, 'y', i)
            if nx == -1:
                nxi = len(X)
            else:
                nxi = n_dict[nx]['x']
            if ny == -1:
                nyi = len(Y)
            else:
                nyi = n_dict[ny]['y']
            mini = min(nxi - xi, nyi - yi)
            if i == 0 and not answer:
                answer.append(str(i))
            else:
                answer.append(str(i) * mini)
            if nx == -1 or ny == -1:
                break
            i = max(nx, ny)
        elif i > 0:
            i -= 1
        else:
            break
    if not answer:
        return "-1"
    return "".join(answer)
