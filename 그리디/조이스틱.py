"""https://programmers.co.kr/learn/courses/30/lessons/42860"""
import string

alphabets = {char: idx for idx, char in enumerate(string.ascii_uppercase)}


def solution(name):
    visited = [1 if c == "A" else 0 for c in name]
    meta = [binary for binary in map(lambda x: int(x != "A"), list(name))]

    answer = 0
    idx = 0
    while not all(visited):
        visited[idx] = 1  # 방문 처리
        if meta[idx] == 1:  # 변화가 필요한 알파벳일 경우
            answer += _get_char_distance("A", name[idx])
        post = _get_nearest_change_point(idx, meta, visited)
        if post is None:
            break
        else:
            idx, distance = post
            answer += distance
    return answer


def _get_char_distance(char1: str, char2: str) -> int:
    """두 알파벳 간 최단거리를 반환하는 함수(방향키를 몇 번 움직여야 하는지)"""
    global alphabets
    d1 = abs(alphabets[char1] - alphabets[char2])
    d2 = 26 - d1  # 알파벳 총 갯수 - d1
    return min([d1, d2])


def _get_nearest_change_point(origin: int, meta: list, visited: list) -> (int, int):
    """
    알파벳 변형이 필요한 가장 가까운 알파벳의 인덱스와 그 알파벳까지의 거리를 반환하는 함수
    - 더이상 변형이 필요없거나 변형할 것이 없는 경우 None을 리턴"""
    if 1 not in meta[:origin] + meta[origin:]:
        return None
    if all(visited[:origin] + visited[origin:]):
        return None
    else:
        # left
        offset = 1
        while not all(visited):
            if (
                meta[_modular(origin - offset, len(meta))] == 1
                and visited[_modular(origin - offset, len(meta))] == 0
            ):
                left = _modular(origin - offset, len(meta))
                break
            offset += 1
        # right

        offset = 1
        while not all(visited):
            if (
                meta[_modular(origin + offset, len(meta))] == 1
                and visited[_modular(origin + offset, len(meta))] == 0
            ):
                right = _modular(origin + offset, len(meta))
                break
            offset += 1

        right_distance = min([abs(right - origin), abs(right - len(meta) - origin)])
        left_distance = min([abs(left - origin), abs(left - len(meta) - origin)])

        if right_distance <= left_distance:
            return right, right_distance
        else:
            return left, left_distance


def _modular(number: int, mod: int):
    """모듈러 함수. _get_nearest_change_point() 함수의 인덱싱 과정에서 IndexError 방지"""
    return number % mod
