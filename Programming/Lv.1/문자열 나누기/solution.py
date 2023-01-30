# https://school.programmers.co.kr/learn/courses/30/lessons/140108
def solution(s):
    answer = 0
    lc, rc = 1, 0
    s = list(s)
    try:
        while s:
            if lc == 1:
                first = s[0]
            s = s[1:]
            letter = s[0]
            if letter == first:
                lc += 1
            else:
                rc += 1
                if lc == rc:
                    answer += 1
                    lc, rc = 1, 0
                    s = s[1:]
    except IndexError:
        answer += 1
    return answer