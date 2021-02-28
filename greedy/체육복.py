"""https://programmers.co.kr/learn/courses/30/lessons/42862"""


def solution(n, lost, reserve):
    """
    우선순위:
    - 번호가 낮은 친구부터 빌려주기 시작
    - 앞사람 체육복을 우선적으로 빌림
    """
    lost, reserve = _clean(sorted(lost), sorted(reserve))
    answer = n - len(lost)

    for l in lost:
        pre, post = l - 1, l + 1
        if pre in reserve:
            answer += 1
            reserve.remove(pre)

        elif post in reserve:
            answer += 1
            reserve.remove(post)
    return answer


def _clean(lost: list, reserve: list) -> (list, list):
    overlap = list(set(lost).intersection(set(reserve)))
    for o in overlap:
        lost.remove(o)
        reserve.remove(o)
    return lost, reserve
