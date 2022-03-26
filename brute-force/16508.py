"""
https://www.acmicpc.net/problem/16508
전공책 제목의 철자를 오려내 단어 만들기
-> 최소 비용으로 만들기

시도1: 철자당 최소 가격 => 그리디한 방법으로 총 가격이 최소가 아닐 수 있음
시도2: 철자 등장하는 책 먼저 찾고 -> NOT systemic
    CASE 1. 철자가 하나라도 등장하지 않으면 -1
    CASE 2. 철자가 모두 등장했으면 최소 가격을 알아내기 위한 브루트포스
시도3: 가격 기준 오름차순 정렬된 책 목록을 linear search. 철자 단위 소거 및 가격 측정. 없으면 -1

엣지케이스:
    동일한 문자가 여러개일 경우
"""
import sys
input = sys.stdin.readline

t = input().strip()
n = int(input())

price_book_list = list()

for _ in range(n):
    price, title = input().split()
    price, title = int(price), title.strip()
    price_book_list.append((price, title))

price_book_list.sort()  # 가격 기준 오름차순 정렬

price_book_list_copy  = price_book_list[:]
for p, b in price_book_list:
    for char in t:
        break
    break

