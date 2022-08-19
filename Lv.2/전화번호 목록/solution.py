# https://school.programmers.co.kr/learn/courses/30/lessons/42577
def compare(p, p2):
    for c, c2 in zip(p, p2):
        if c != c2:
            return True
        
    return False

def solution(phone_book):
    phone_book.sort()
    
    for i, p in enumerate(phone_book):
        try:
            if not compare(p, phone_book[i+1]):
                return False
        except IndexError:
            break
        
    return True