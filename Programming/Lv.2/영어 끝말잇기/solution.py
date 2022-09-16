# https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    dictionary = {}
    
    for i, word in enumerate(words):
        if i > 0 and words[i - 1][-1] != word[0]:
            return [(i % n) + 1, (i // n) + 1]
        
        if word not in dictionary:
            dictionary[word] = 1
        else:
            return [(i % n) + 1, (i // n) + 1]
        
    return [0, 0]