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


# startswith 라는 함수가 있구나
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True