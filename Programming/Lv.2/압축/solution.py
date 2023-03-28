# https://school.programmers.co.kr/learn/courses/30/lessons/17684
def solution(msg):
    d = {}
    a = []
    for n in range(26):
        alphabet = chr(ord('A') + n)
        d[alphabet] = n
        a.append(alphabet)
    answer = []
    index = 0
    for i, letter in enumerate(msg):
        if index > i:
            continue
        new_letter = letter
        while True:
            if new_letter in d:
                letter = new_letter
                if i == len(msg) - 1:
                    index += 1
                    answer.append(d[letter] + 1)
                    break
                i += 1
                index += 1
                new_letter = letter + msg[i]
            else:
                d[new_letter] = len(a)
                a.append(new_letter)
                answer.append(d[letter] + 1)
                break
    return answer