'''https://programmers.co.kr/learn/courses/30/lessons/42579
* 노래 수록 기준
1. [장르 순서]속한 노래가 많이 재생된 장르를 먼저 수록
2. [노래 순서]장르 내에서 많이 재생된 노래를 먼저 수록
3. [중복 시 낮은 ID순] 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
* 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 

genres/plays[i]: 고유번호 i인 노래의 장르/재생횟수
'''
from collections import Counter

def solution(genres, plays):
    ids = range(len(genres))
    result = []
    merge = list(map(lambda x: [x, genres[x], plays[x]], ids))

    # 장르 순서
    sums = []
    for genre in set(map(lambda x: x[1], merge)):
        sums.append((genre, sum(map(lambda x: x[-1], filter(lambda x: x[1]==genre, merge)))))

    # 노래 순서 & 중복 시 낮은 ID 순 정렬
    for genre, _ in sorted(sums, key=lambda x: x[-1], reverse=True):
        order = sorted(sorted(filter(lambda x: x[1]==genre, merge), key=lambda x: x[0]), key=lambda x: x[-1], reverse=True)
        result.extend(list(map(lambda x: x[0], order[:2])))
    return result