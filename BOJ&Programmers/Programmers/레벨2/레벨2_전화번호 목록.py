def solution(phone_book):
    answer = True
    phone_book.sort()
    for pb1, pb2 in zip(phone_book, phone_book[1:]):
        if pb2.startswith(pb1):
            return False

    return answer