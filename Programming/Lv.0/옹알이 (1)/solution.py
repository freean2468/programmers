def solution(babbling):
    possible = ['aya', 'ye', 'woo', 'ma']
    for p in possible:
        for i, b in enumerate(babbling):
            if p in b:
                babbling[i] = babbling[i].replace(p, ' ')
    for i, b in enumerate(babbling):
        babbling[i] = babbling[i].replace(' ', '')
    return len(list(filter(lambda x:x == '', babbling)))
