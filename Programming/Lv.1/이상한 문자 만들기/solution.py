# https://school.programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    answer = []
    for sen in s.split(' '):
        sentence = []
        for i, c in enumerate(sen):
            sentence.append(c.upper() if i % 2 == 0 else c.lower())
            
        answer.append(''.join(sentence))
            
    return ' '.join(answer)