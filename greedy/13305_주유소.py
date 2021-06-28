'''https://www.acmicpc.net/problem/13305
문제:
    - N개 도시에 대하여 가장 왼쪽 도시에서 가장 오른쪽 도시까지 자동차를 통해 이동할 때,
      사용되는 기름값의 최소비용
    - 주유소에서 기름을 넣고 출발, 자동차의 기름통 용량은 무제한
    - 도로를 통해 이동할 때 1km당 1L의 기름 사용
    - 각 도시는 하나의 주유소 보유. 리터당 기름값이 도시마다 다름

입력:
    - 도시 개수. 2 이상 10만 이하
    - 도로별 길이. 1 이상 10억 이하
    - 도시별 기름값. 1 이상 10억 이하

생각:
    - 그리디의 기준을 정해야지
    - 룩업 과정에서 기준 도시보다 기름값이 낮은 도시가 나오기 전까지는 이걸로 필요한 만큼 다 채움
'''
from collections import deque

n = int(input()) # 도시 개수
road_lengths = deque(list(map(int, input().split())) + [0]) # 도로(인덱싱 편의상 마지막 패딩)
city_prices = deque(list(map(int, input().split()))) # 도시별 리터당 기름값

min_price = int(1e+9)
total_value = 0
while city_prices:
    price = city_prices.popleft()
    length = road_lengths.popleft()

    if min_price > price:
        min_price = price
    
    total_value += length * min_price

print(total_value)
    


