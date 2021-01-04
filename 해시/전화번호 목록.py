"""https://programmers.co.kr/learn/courses/30/lessons/42577"""


def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    for idx, v in enumerate(tuple(phone_book)):
        if tuple(filter(lambda x: x.startswith(v), phone_book[idx + 1 :])):
            return False
    return True